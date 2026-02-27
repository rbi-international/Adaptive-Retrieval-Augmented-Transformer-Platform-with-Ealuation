from qdrant_client import QdrantClient
from packages.core.config import get_settings


class VectorStore:
    def __init__(self):
        settings = get_settings()
        self.client = QdrantClient(url=settings.qdrant_url)

    def health_check(self) -> bool:
        try:
            self.client.get_collections()
            return True
        except Exception:
            return False