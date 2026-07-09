from src.pdf_loader import read_pdf
from src.chunker import chunk_text
from src.embeddings import generate_embedding
from src.vector_store import create_vector_store, search
from src.llm import generate_answer


class PlacementMentor:

    def __init__(self, pdf_path):

        text = read_pdf(pdf_path)

        self.chunks = chunk_text(text, chunk_size=500)

        embeddings = [
            generate_embedding(chunk)
            for chunk in self.chunks
        ]

        self.index = create_vector_store(embeddings)

    def ask(self, question):

        query_embedding = generate_embedding(question)

        distances, indices = search(
            self.index,
            query_embedding
        )

        context = ""

print("\n" + "="*80)
print("Retrieved Chunks")
print("="*80)

for i, idx in enumerate(indices[0]):

    print(f"\nChunk {i+1} (Index: {idx})")
    print("-"*50)
    print(self.chunks[idx][:300])   # First 300 characters
    print()

    context += self.chunks[idx] + "\n\n"

print("="*80)

return generate_answer(context, question)
    