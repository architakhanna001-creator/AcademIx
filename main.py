from flask import Flask, render_template, request
import os

from utils.pdf_reader import extract_text
from utils.summarizer import summarize_notes
from utils.flashcards import generate_flashcards

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    pdf = request.files["pdf_file"]

    if pdf.filename == "":
        return "No file selected."

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], pdf.filename)

    pdf.save(file_path)

    # Extract text
    extracted_text = extract_text(file_path)

    # Generate summary
    summary = summarize_notes(extracted_text)

    # Generate flashcards
    flashcards = generate_flashcards(extracted_text)

    return render_template(
        "result.html",
        filename=pdf.filename,
        summary=summary,
        flashcards=flashcards,
        extracted_text=extracted_text
    )


if __name__ == "__main__":
    app.run(debug=True)