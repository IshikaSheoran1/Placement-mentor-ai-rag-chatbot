from sentence_transformers import SentenceTransformer

#Load the embedding model
model=SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text):
    """
    Converts text into an embedding vector.
    """
    embedding=model.encode(text)

    return embedding