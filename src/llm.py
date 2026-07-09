import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(context, question):
    """
    Generates an answer using Gemini based only on the retrieved context.
    """

    prompt = f"""
You are an AI placement assistant.

Answer ONLY using the context below.

If the answer is not present in the context, reply:
"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text