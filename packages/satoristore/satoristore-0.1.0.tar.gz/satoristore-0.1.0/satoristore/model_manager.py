import threading
from typing import Any, Tuple
from PIL import Image
import torch


class ModelManager:
    """
    A singleton class responsible for loading and managing embedding models.
    Ensures models are loaded only once and can be shared across instances.
    """

    _instance = None
    _lock = threading.Lock()
    _models = {}
    _model_locks = {}

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(ModelManager, cls).__new__(cls)
        return cls._instance

    def load_text_model(self, model_name: str = "all-MiniLM-L6-v2") -> Any:
        """
        Loads or retrieves the text embedding model.
        Implements lazy loading and thread safety.

        Parameters:
        - model_name: Name of the text embedding model to load.

        Returns:
        - The loaded text embedding model.
        """
        if model_name not in self._models:
            # Ensure thread safety during model loading
            if model_name not in self._model_locks:
                self._model_locks[model_name] = threading.Lock()
            with self._model_locks[model_name]:
                if model_name not in self._models:
                    from sentence_transformers import SentenceTransformer

                    self._models[model_name] = SentenceTransformer(
                        model_name,
                        tokenizer_kwargs={"clean_up_tokenization_spaces": True},
                    )
        return self._models[model_name]

    def get_text_embedding_size(self, model_name: str = "all-MiniLM-L6-v2") -> int:
        model = self._models.get(model_name)
        if model:
            return model.get_sentence_embedding_dimension()
        else:
            raise ValueError(f"Text model '{model_name}' not loaded.")

    def load_multimodal_model(
        self, model_name: str = "openai/clip-vit-base-patch32"
    ) -> Tuple[Any, Any, str]:
        """
        Loads or retrieves the multimodal (CLIP) embedding model using Hugging Face transformers.
        Implements lazy loading and thread safety.

        Parameters:
        - model_name: Name of the CLIP model to load.

        Returns:
        - A tuple containing the model, processor, and device information.
        """
        if "multimodal_model" not in self._models:
            # Ensure thread safety during model loading
            if "multimodal_model" not in self._model_locks:
                self._model_locks["multimodal_model"] = threading.Lock()
            with self._model_locks["multimodal_model"]:
                if "multimodal_model" not in self._models:
                    import torch
                    from transformers import CLIPModel, CLIPProcessor

                    device = torch.device(
                        "cuda" if torch.cuda.is_available() else "cpu"
                    )
                    model = CLIPModel.from_pretrained(model_name)
                    model.to(device)
                    processor = CLIPProcessor.from_pretrained(model_name)
                    self._models["multimodal_model"] = model
                    self._models["multimodal_processor"] = processor
                    self._models["device"] = device
        return (
            self._models["multimodal_model"],
            self._models["multimodal_processor"],
            self._models["device"],
        )

    def get_multimodal_embedding_size(self) -> int:
        """
        Returns the dimensionality of the image embedding model.
        """
        model = self._models.get("multimodal_model")
        if model:
            processor = self._models.get("multimodal_processor")
            image = Image.new("RGB", (100, 100), color="red")
            image_input = processor(
                images=image, return_tensors="pt", padding=True, truncation=True
            )
            with torch.no_grad():
                embedding = model.get_image_features(**image_input)
            return embedding.shape[1]  # Return the second dimension of the output
        else:
            raise ValueError("Multimodal model not loaded.")
