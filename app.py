import streamlit as st
import tempfile
from chatbot import PlacementMentor

st.set_page_config(
    page_title="Placement Mentor AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Placement Mentor AI")

st.write("Upload your placement PDF and ask questions.")

uploaded_file= st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path=tmp_file.name

if uploaded_file is not None:

    if (
        "bot" not in st.session_state
        or
        "current_pdf" not in st.session_state
        or
        st.session_state.current_pdf != uploaded_file.name
    ):

        with st.spinner("Processing PDF..."):

            st.session_state.bot = PlacementMentor(pdf_path)

            st.session_state.current_pdf = uploaded_file.name

        st.success("✅ PDF processed successfully!")


if uploaded_file is not None:

    question = st.text_input(
        "Ask a question about the uploaded document"
    )

    if st.button("Ask"):

        if question.strip():

            with st.spinner("Thinking..."):

                answer = st.session_state.bot.ask(question)

            st.markdown("## 🤖 Answer")

            st.write(answer)

else:

    st.info("📄 Please upload a PDF first.")