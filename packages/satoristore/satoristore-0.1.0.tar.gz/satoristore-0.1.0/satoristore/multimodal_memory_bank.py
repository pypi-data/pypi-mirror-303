import os
import io
import json
import logging
import numpy as np
import uuid
from PIL import Image
from typing import Any, Dict, List, Optional
from datetime import datetime

from qdrant_client import QdrantClient
from qdrant_client.http import models

import torch
from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    LargeBinary,
    ForeignKey,
    create_engine,
    Index,
    JSON,
)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base

from satoristore.memory_bank import MemoryBank

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

Base = declarative_base()


class MemoryUnit(Base):
    __tablename__ = "memory_units"
    unique_id = Column(String, primary_key=True)
    timestamp = Column(DateTime, nullable=False)

    # Inputs
    type = Column(String, nullable=False)
    description = Column(Text)
    metadata_ = Column("metadata", JSON)
    state_before = Column(LargeBinary)

    # Outputs
    status = Column(String)
    state_after = Column(LargeBinary)
    human_comment = Column(Text)
    ai_comment = Column(Text)

    # Relationships
    parent_id = Column(String, ForeignKey("memory_units.unique_id"))
    parent = relationship("MemoryUnit", remote_side=[unique_id], backref="children")
    media_blobs = relationship("MediaBlob", back_populates="memory_unit")

    __table_args__ = (
        Index("ix_memory_units_timestamp", "timestamp"),
        Index("ix_memory_units_type", "type"),
        Index("ix_memory_units_status", "status"),
        Index("ix_memory_units_parent_id", "parent_id"),
    )


class MediaBlob(Base):
    __tablename__ = "media_blobs"
    id = Column(String, primary_key=True)
    memory_unit_id = Column(String, ForeignKey("memory_units.unique_id"))
    media_data = Column(LargeBinary)
    media_type = Column(String)

    memory_unit = relationship("MemoryUnit", back_populates="media_blobs")


class MultimodalMemoryBank(MemoryBank):
    """
    MultimodalMemoryBank handles storage and retrieval of memory units containing both textual
    and multimedia data. It uses SQLAlchemy for structured data storage and Qdrant for vector embeddings
    to enable similarity searches.
    """

    def __init__(self, home_dir: str = None):
        """
        Initialize the MultimodalMemoryBank with specified models.

        Parameters:
        - model_name (str): Name of the CLIP model to use for embeddings.
        """
        super().__init__(home_dir)
        self.collection_name = "multimodal_memory_units"
        self.image_model, self.image_processor, _ = (
            self.model_manager.load_multimodal_model()
        )
        self.text_model = self.model_manager.load_text_model()
        self.text_embedding_size = self.model_manager.get_text_embedding_size()
        self.image_embedding_size = self.model_manager.get_multimodal_embedding_size()
        self.supports_media_blobs = True
        self.engine = None
        self.Session = None
        self.initialize()

    def initialize(self):
        try:
            os.makedirs(self.home_dir, exist_ok=True)
            self._initialize_sqlalchemy()
            self._initialize_qdrant()
            self.initialized = True
        except Exception as e:
            logger.error(f"Error initializing MultimodalMemoryBank: {e}")
            raise e

    def store(self, data: Dict[str, Any]) -> str:
        """
        Store a memory unit in the database.

        Parameters:
        - data: Dictionary containing the memory unit data.

        Returns:
        - The unique_id of the stored memory unit.
        """
        self._ensure_initialized()
        if "unique_id" not in data:
            unique_id = self._generate_unique_id()
        else:
            unique_id = data["unique_id"]

        try:
            with self.Session() as session:
                memory_unit = MemoryUnit(
                    unique_id=unique_id,
                    timestamp=data.get("timestamp", datetime.utcnow()),
                    type=data.get("type"),
                    description=data.get("description", ""),
                    status=data.get("status", ""),
                    parent_id=data.get("parent_id"),
                    metadata_=data.get("metadata", {}),
                    state_before=(
                        data.get("state_before").tobytes()
                        if isinstance(data.get("state_before"), Image.Image)
                        else data.get("state_before")
                    ),
                    state_after=(
                        data.get("state_after").tobytes()
                        if isinstance(data.get("state_after"), Image.Image)
                        else data.get("state_after")
                    ),
                    human_comment=data.get("human_comment", ""),
                    ai_comment=data.get("ai_comment", ""),
                )
                session.add(memory_unit)

                # Add media blobs
                media_blobs = data.get("media_blobs", [])
                for media_blob in media_blobs:
                    blob = MediaBlob(
                        id=media_blob.get("id"),
                        memory_unit_id=unique_id,
                        media_data=(
                            media_blob.get("media_data").tobytes()
                            if isinstance(media_blob.get("media_data"), Image.Image)
                            else media_blob.get("media_data")
                        ),
                        media_type=media_blob.get("media_type"),
                    )
                    session.add(blob)

                session.commit()
            return unique_id
        except SQLAlchemyError as e:
            logger.error(f"Error storing memory unit '{unique_id}': {e}")
            raise e

    def retrieve_by_id(
        self, unique_id: str, depth: int = 1
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieve the memory unit by unique ID from the database.

        Parameters:
        - unique_id: The unique identifier of the memory unit.
        - depth: The depth of child units to retrieve.

        Returns:
        - A dictionary representing the memory unit, or None if not found.
        """
        return self._fetch_unit(unit_id=unique_id, current_depth=0, depth=depth)

    def embed(self, unique_id: str, data: Dict[str, Any]) -> None:
        """
        Generate embeddings for the memory unit and store them in Qdrant.

        Parameters:
        - unique_id: Unique identifier for the memory unit.
        - data: Dictionary containing the memory unit data.
        """
        self._ensure_initialized()
        try:
            vectors = {}
            input_text_embeddings_list = []
            output_text_embeddings_list = []
            all_text_embeddings_list = []
            input_image_embeddings_list = []
            output_image_embeddings_list = []
            all_image_embeddings_list = []
            input_fields = ["type", "description", "metadata", "state_before"]
            output_fields = ["status", "human_comment", "ai_comment", "state_after"]
            all_fields = input_fields + output_fields

            # Function to embed image data

            for field in all_fields:
                content = data.get(field)
                if content:
                    if field == "metadata":
                        # Convert metadata dict to string if necessary
                        if isinstance(content, dict):
                            content = json.dumps(content)

                    if field in ["state_before", "state_after"]:
                        embedding = self._embed_image(content)
                        vectors[field] = embedding.tolist()
                        if field in input_fields:
                            input_image_embeddings_list.append(embedding)
                        else:
                            output_image_embeddings_list.append(embedding)
                    else:
                        embedding = self._embed_text(content)
                        vectors[field] = embedding.tolist()
                        if field in input_fields:
                            input_text_embeddings_list.append(embedding)
                        else:
                            output_text_embeddings_list.append(embedding)
                        all_text_embeddings_list.append(embedding)

            if input_text_embeddings_list or input_image_embeddings_list:
                text_embedding = (
                    np.mean(input_text_embeddings_list, axis=0)
                    if input_text_embeddings_list
                    else np.zeros(self.text_embedding_size)
                )
                image_embedding = (
                    np.mean(input_image_embeddings_list, axis=0)
                    if input_image_embeddings_list
                    else np.zeros(self.image_embedding_size)
                )
                vectors["inputs"] = np.concatenate(
                    [text_embedding, image_embedding]
                ).tolist()

            if output_text_embeddings_list or output_image_embeddings_list:
                text_embedding = (
                    np.mean(output_text_embeddings_list, axis=0)
                    if output_text_embeddings_list
                    else np.zeros(self.text_embedding_size)
                )
                image_embedding = (
                    np.mean(output_image_embeddings_list, axis=0)
                    if output_image_embeddings_list
                    else np.zeros(self.image_embedding_size)
                )
                vectors["outputs"] = np.concatenate(
                    [text_embedding, image_embedding]
                ).tolist()

            if all_text_embeddings_list or all_image_embeddings_list:
                text_embedding = (
                    np.mean(all_text_embeddings_list, axis=0)
                    if all_text_embeddings_list
                    else np.zeros(self.text_embedding_size)
                )
                image_embedding = (
                    np.mean(all_image_embeddings_list, axis=0)
                    if all_image_embeddings_list
                    else np.zeros(self.image_embedding_size)
                )
                vectors["all"] = np.concatenate(
                    [text_embedding, image_embedding]
                ).tolist()

            # Process media blobs
            media_blobs = data.get("media_blobs", [])
            image_embeddings = []
            if media_blobs:
                for media in media_blobs:
                    if media.get("media_type") == "image":
                        image_data = media.get("media_data")
                        embedding = self._embed_image(image_data)
                        if embedding is not None:
                            image_embeddings.append(embedding)

                if image_embeddings:
                    # Average the image embeddings
                    image_embedding = np.mean(image_embeddings, axis=0)
                    vectors["media_blobs"] = image_embedding.tolist()

            # Upsert embeddings into Qdrant with named vectors
            point = models.PointStruct(
                id=unique_id,
                vector=vectors,
                payload={"unique_id": unique_id, "type": data.get("type")},
            )

            self.qdrant_client.upsert(
                collection_name=self.collection_name, points=[point]
            )

        except Exception as e:
            logger.error(f"Error embedding memory unit: {e}")
            raise e

    def retrieve_similar(
        self,
        query_data: Dict[str, Any],
        query_weights: Dict[str, float] = {},
        filter_data: Dict[str, Any] = {},
        max_results: int = 10,
        score_threshold: float = 0.5,
    ) -> List[str]:
        """
        Retrieve IDs of similar memory units based on the provided query, along with their scores.

        Parameters:
        - query_data: A dictionary containing the query to use for similarity search.
        - query_weights: A dictionary containing the weights to use for similarity search.
        - filter_data: A dictionary containing the data to filter the results by.
        - max_results: The maximum number of results to return.
        - score_threshold: The minimum score threshold for the results.

        Returns:
        - A list of tuples representing similar memory units and their scores.
        """
        self._ensure_initialized()
        # collect all filter_data into conditions
        conditions = []
        for field, value in filter_data.items():
            conditions.append(
                models.FieldCondition(key=field, match=models.MatchValue(value=value))
            )
        if conditions:
            filter = models.Filter(must=conditions)
        else:
            filter = None

        # make independent query for each field in query_data with max_results * len(query_data)
        results = {}
        factor = len(query_data)
        for field, value in query_data.items():
            if isinstance(value, Image.Image):
                query_embedding = self._embed_image(value)
            else:
                query_embedding = self._embed_text(value)
            query_results = self.qdrant_client.search(
                collection_name=self.collection_name,
                query_vector=(field, query_embedding),
                limit=max_results * factor,
                score_threshold=score_threshold,
                query_filter=filter,
            )
            for hit in query_results:
                id = hit.payload["unique_id"]
                score = hit.score
                if id not in results:
                    results[id] = {}
                results[id][field] = score

        # calculate the total weight of the query
        total_weight = 0
        for field in query_data:
            total_weight += query_weights[field] if field in query_weights else 1

        # combine results with a simple weighted average
        combined_results = []
        for id, scores in results.items():
            if len(scores) == len(query_data):
                combined_score = 0
                for field, score in scores.items():
                    combined_score += score * (
                        query_weights[field] if field in query_weights else 1
                    )
                combined_results.append((id, combined_score / total_weight))

        # return the top N sorted combined results
        filtered_results = [
            (id, score) for id, score in combined_results if score > score_threshold
        ]
        sorted_results = sorted(filtered_results, key=lambda x: x[1], reverse=True)

        return sorted_results[:max_results]

    def delete(self, unique_id: str) -> None:
        """
        Delete a memory unit and its associated data.

        Parameters:
        - unique_id (str): The unique ID of the memory unit to delete.
        """
        self._ensure_initialized()
        try:
            with self.Session() as session:
                memory_unit = (
                    session.query(MemoryUnit)
                    .filter_by(unique_id=unique_id)
                    .one_or_none()
                )
                if memory_unit:
                    session.delete(memory_unit)
                    session.commit()
                else:
                    logger.warning(
                        f"Memory unit with ID {unique_id} not found in database."
                    )

            # Delete embeddings from Qdrant
            self.qdrant_client.delete(
                collection_name=self.collection_name,
                points_selector=models.PointIdsList(points=[unique_id]),
            )
        except Exception as e:
            logger.error(f"Error deleting memory unit '{unique_id}': {e}")
            raise e

    def edit(self, unique_id: str, data: Dict[str, Any]) -> None:
        """
        Edit the memory unit with the specified unique ID using the provided data.

        Parameters:
        - unique_id: The unique identifier of the memory unit to edit.
        - data: A dictionary containing the updated data.
        """
        self._ensure_initialized()
        try:
            with self.Session() as session:
                memory_unit = (
                    session.query(MemoryUnit)
                    .filter_by(unique_id=unique_id)
                    .one_or_none()
                )
                if memory_unit is None:
                    raise ValueError(
                        f"Memory unit with unique_id {unique_id} not found."
                    )

                # Update memory unit fields
                for key, value in data.items():
                    if key == "metadata":
                        setattr(memory_unit, "metadata_", value)
                    elif key == "state_before":
                        setattr(
                            memory_unit,
                            "state_before",
                            (
                                value.tobytes()
                                if isinstance(value, Image.Image)
                                else value
                            ),
                        )
                    elif key == "state_after":
                        setattr(
                            memory_unit,
                            "state_after",
                            (
                                value.tobytes()
                                if isinstance(value, Image.Image)
                                else value
                            ),
                        )
                    elif hasattr(memory_unit, key) and key != "media_blobs":
                        setattr(memory_unit, key, value)

                # Handle media blobs
                if "media_blobs" in data:
                    # Remove existing media blobs
                    session.query(MediaBlob).filter_by(
                        memory_unit_id=unique_id
                    ).delete()

                    # Add new media blobs
                    for media_blob in data["media_blobs"]:
                        blob = MediaBlob(
                            id=media_blob.get("id"),
                            memory_unit_id=unique_id,
                            media_data=(
                                media_blob.get("media_data").tobytes()
                                if isinstance(media_blob.get("media_data"), Image.Image)
                                else media_blob.get("media_data")
                            ),
                            media_type=media_blob.get("media_type"),
                        )
                        session.add(blob)

                session.commit()

            # Update embeddings in Qdrant
            self.qdrant_client.delete(
                collection_name=self.collection_name, points_selector=[unique_id]
            )
            self.embed(unique_id, data)
        except SQLAlchemyError as e:
            logger.error(f"Error editing memory unit '{unique_id}': {e}")
            raise e

    def close(self):
        """
        Close the database connection and other resources.
        """
        if self.engine:
            self.engine.dispose()
        if self.qdrant_client:
            self.qdrant_client.close()

    def _fetch_unit(
        self,
        unit_id: str,
        current_depth: int,
        depth: int,
        visited: Optional[set] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Fetches a memory unit recursively up to the specified depth.

        Parameters:
        - unit_id: The unique identifier of the memory unit.
        - current_depth: The current depth of recursion.
        - depth: The maximum depth to recurse.
        - visited: A set of visited unit_ids to prevent cycles.

        Returns:
        - A dictionary representing the memory unit, or None if not found.

        Raises:
        - Exception: If an error occurs during database operations.
        """
        self._ensure_initialized()

        if visited is None:
            visited = set()

        if unit_id in visited:
            logger.warning(
                f"Cycle detected while fetching unit {unit_id}. Skipping to prevent infinite recursion."
            )
            return None

        visited.add(unit_id)

        try:
            with self.Session() as session:
                # Fetch the unit
                memory_unit = (
                    session.query(MemoryUnit).filter_by(unique_id=unit_id).one_or_none()
                )
                if not memory_unit:
                    logger.warning(f"Memory unit with ID {unit_id} not found.")
                    return None

                # Convert SQLAlchemy object to dictionary
                unit = memory_unit.__dict__.copy()
                unit.pop("_sa_instance_state", None)

                # If using 'metadata_' attribute, map it back to 'metadata'
                if "metadata_" in unit:
                    unit["metadata"] = unit.pop("metadata_", None)

                # Fetch media blobs if supported
                if self.supports_media_blobs:
                    # Convert state_before and state_after to PIL Image if they exist
                    if unit.get("state_before"):
                        try:
                            unit["state_before"] = Image.open(
                                io.BytesIO(unit["state_before"])
                            )
                        except Exception as e:
                            logger.error(
                                f"Error converting state_before to PIL Image: {e}"
                            )

                    if unit.get("state_after"):
                        try:
                            unit["state_after"] = Image.open(
                                io.BytesIO(unit["state_after"])
                            )
                        except Exception as e:
                            logger.error(
                                f"Error converting state_after to PIL Image: {e}"
                            )

                    unit["media_blobs"] = []
                    for media_blob in memory_unit.media_blobs:
                        blob_dict = media_blob.__dict__.copy()
                        blob_dict.pop("_sa_instance_state", None)
                        if blob_dict["media_data"] and blob_dict[
                            "media_type"
                        ].startswith("image/"):
                            try:
                                blob_dict["media_data"] = Image.open(
                                    io.BytesIO(blob_dict["media_data"])
                                )
                            except Exception as e:
                                logger.error(
                                    f"Error converting media_data to PIL Image: {e}"
                                )
                        unit["media_blobs"].append(blob_dict)

                # Fetch descendants if depth allows
                if current_depth < depth:
                    unit["subunits"] = []
                    child_units = (
                        session.query(MemoryUnit).filter_by(parent_id=unit_id).all()
                    )
                    for child_unit in child_units:
                        try:
                            child_data = self._fetch_unit(
                                child_unit.unique_id, current_depth + 1, depth, visited
                            )
                            if child_data:
                                unit["subunits"].append(child_data)
                        except Exception as e:
                            logger.error(
                                f"Error fetching child unit with ID {child_unit.unique_id}: {e}"
                            )
                            continue  # Skip this child and continue with others
                return unit
        except SQLAlchemyError as e:
            logger.error(f"Error fetching unit with ID {unit_id}: {e}")
            raise  # Re-raise the exception after logging

    def _initialize_qdrant(self):
        # Initialize qdrant
        if self.qdrant_client is None:
            self.qdrant_client = QdrantClient(path=self.qdrant_path)

        # Define vector configurations for each named vector
        vector_configs = {
            # Inputs
            "type": models.VectorParams(
                size=self.text_embedding_size, distance=models.Distance.COSINE
            ),
            "description": models.VectorParams(
                size=self.text_embedding_size, distance=models.Distance.COSINE
            ),
            "metadata": models.VectorParams(
                size=self.text_embedding_size, distance=models.Distance.COSINE
            ),
            "state_before": models.VectorParams(
                size=self.image_embedding_size, distance=models.Distance.COSINE
            ),
            # Outputs
            "status": models.VectorParams(
                size=self.text_embedding_size, distance=models.Distance.COSINE
            ),
            "human_comment": models.VectorParams(
                size=self.text_embedding_size, distance=models.Distance.COSINE
            ),
            "ai_comment": models.VectorParams(
                size=self.text_embedding_size, distance=models.Distance.COSINE
            ),
            "state_after": models.VectorParams(
                size=self.image_embedding_size, distance=models.Distance.COSINE
            ),
            # Combined embeddings
            "inputs": models.VectorParams(
                size=self.text_embedding_size + self.image_embedding_size,
                distance=models.Distance.COSINE,
            ),
            "outputs": models.VectorParams(
                size=self.text_embedding_size + self.image_embedding_size,
                distance=models.Distance.COSINE,
            ),
            "all": models.VectorParams(
                size=self.text_embedding_size + self.image_embedding_size,
                distance=models.Distance.COSINE,
            ),
            # Media blobs and state images
            "media_blobs": models.VectorParams(
                size=self.image_embedding_size, distance=models.Distance.COSINE
            ),
        }

        if not self.qdrant_client.collection_exists(self.collection_name):
            # Create collection with multiple vectors
            self.qdrant_client.create_collection(
                collection_name=self.collection_name, vectors_config=vector_configs
            )

    def _initialize_sqlalchemy(self):
        """
        Initialize the SQLAlchemy engine and session factory.
        """
        self.engine = create_engine(
            f"sqlite:///{self.db_path}", connect_args={"check_same_thread": False}
        )
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

        logger.debug(f"Database path: {self.db_path}")
        logger.debug(f"Database file permissions: {oct(os.stat(self.db_path).st_mode)}")

    def _generate_unique_id(self) -> str:
        return str(uuid.uuid4())

    def _embed_text(self, text: str) -> np.ndarray:
        return self.text_model.encode([text])[0]

    def _embed_image(self, image: Image.Image) -> np.ndarray:
        if image:
            image_input = self.image_processor(
                images=image, return_tensors="pt", padding=True, truncation=True
            )
            with torch.no_grad():
                embedding = self.image_model.get_image_features(**image_input)
            return embedding.numpy().flatten()
        return None
