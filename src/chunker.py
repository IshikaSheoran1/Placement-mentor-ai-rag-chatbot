def chunk_text(text, chunk_size=1000):
    """
    Splits text into fixed-size chunks.
    """

    chunks = []

    for start in range(0, len(text), chunk_size):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)

    return chunks