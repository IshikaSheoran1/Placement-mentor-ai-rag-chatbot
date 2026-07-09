from pypdf import PdfReader


def read_pdf(pdf_path):
    """
    Reads a PDF file and returns all extracted text.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text