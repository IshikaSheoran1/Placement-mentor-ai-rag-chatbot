import faiss
import numpy as np

def create_vector_store(embeddings):
    """create a FAISS index from embeddings."""

    dimension=len(embeddings[0])

    index=faiss.IndexFlatL2(dimension)

    embeddings=np.array(embeddings).astype("float32")

    index.add(embeddings)

    return index


def search(index, query_embedding, k=3):
    """
    Searches the vector store.
    """

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    return distances, indices