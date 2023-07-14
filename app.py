import gradio as gr
import pdfminer
from pdfminer.high_level import extract_text


def read_pdf(file):
    return extract_text(file.name)


iface = gr.Interface(
    read_pdf,
    gr.inputs.File(label="Upload a PDF file"),
    gr.outputs.Textbox(label="Extracted text"),
    title="PDF Text Extractor",
    description="A smooth app that gets text from PDF files using pdfminer🧠",
    theme="ParityError/Anime",

)
iface.launch()
