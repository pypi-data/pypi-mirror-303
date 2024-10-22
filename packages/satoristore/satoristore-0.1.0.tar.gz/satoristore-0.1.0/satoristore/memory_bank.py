import threading
import logging
from abc import ABC, abstractmethod
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from satoristore.model_manager import ModelManager

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class MemoryBank(ABC):
    """
    An abstract base class defining the interface for embedding and retrieval operations.
    Ensures consistency across different memory bank implementations.
    """

    def __init__(self, home_dir: str = None):
        self.initialized = False
        self.home_dir = home_dir or os.environ.get(
            "SATORISTORE_HOME", str(Path.home() / ".satoristore")
        )
        self.db_path = os.path.join(self.home_dir, "satoristore.db")
        self.qdrant_path = os.path.join(self.home_dir, "qdrant")
        self.lock = threading.Lock()
        self.conn = None
        self.qdrant_client = None
        self.model_manager = ModelManager()
        self.model = None
        self.collection_name = None
        self.initialized = False
        self.supports_media_blobs = False

    ###########
    # Classes #
    ###########

    @abstractmethod
    def initialize(self):
        """
        Initialize the database connections and ensure necessary tables and collections exist.
        """
        pass

    @abstractmethod
    def store(self, unique_id: str, data: Dict[str, Any]) -> str:
        """
        Store the memory unit data in SQLite.

        Parameters:
        - unique_id: Unique identifier for the memory unit.
        - data: A dictionary containing the data to be stored.

        Returns:
        - The unique ID of the stored memory unit.
        """
        pass

    @abstractmethod
    def retrieve_by_id(
        self, unique_id: str, depth: int = 1
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieve the memory unit by unique ID from SQLite, including descendants up to the specified depth.

        Parameters:
        - unique_id: The unique identifier of the memory unit.
        - depth: The depth of descendants to retrieve.

        Returns:
        - A dictionary representing the memory unit and its descendants, or None if not found.
        """
        pass

    @abstractmethod
    def embed(self, unique_id: str, data: Dict[str, Any]) -> None:
        """
        Generate embeddings for the memory unit and store them in Qdrant.

        Parameters:
        - unique_id: Unique identifier for the memory unit.
        - data: A dictionary containing the data to be embedded.
        """
        pass

    def retrieve_similar(
        self,
        query_data: Dict[str, Any],
        query_weights: Dict[str, float] = {},
        filter_data: Dict[str, Any] = {},
        max_results: int = 10,
        score_threshold: float = 0.5,
    ) -> List[Tuple[str, float]]:
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
        pass

    @abstractmethod
    def delete(self, unique_id: str, delete_from_qdrant: bool = True) -> None:
        """
        Delete the memory unit with the specified unique ID from both SQLite and Qdrant.

        Parameters:
        - unique_id: The unique identifier of the memory unit to delete.
        """
        pass

    @abstractmethod
    def edit(self, unique_id: str, data: Dict[str, Any]) -> None:
        """
        Edit the memory unit with the specified unique ID using the provided data.

        Parameters:
        - unique_id: The unique identifier of the memory unit to edit.
        - data: A dictionary containing the updated data.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Close the database connection and other resources.
        """
        pass

    ###########
    # Methods #
    ###########

    def close_unit(self, unique_id: str, data: Dict[str, Any]) -> None:
        """
        Close the memory unit, updating its status and any final data.

        Parameters:
        - unique_id: The unique identifier of the memory unit to close.
        - data: A dictionary containing the data to update upon closing.
        """
        self.edit(unique_id, data)

    def _ensure_initialized(self):
        if not self.initialized:
            self.initialize()
            self.initialized = True
