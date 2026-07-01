from flask import Flask, render_template, request, send_file
import os
from io import BytesIO

from utils.pdf_reader import extract_text
from utils.study_generator import generate_study_material
from utils.pdf_export import generate_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store latest generated content
latest_summary = ""
latest_flashcards = []
latest_quiz = []
latest_notes = ""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    global latest_summary
    global latest_flashcards
    global latest_quiz
    global latest_notes

    pdf = request.files["pdf_file"]

    if pdf.filename == "":
        return "No file selected."

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], pdf.filename)
    pdf.save(file_path)

    text = extract_text(file_path)

    latest_notes = text

    try:

        study_material = generate_study_material(text)

        latest_summary = study_material["summary"]
        latest_flashcards = study_material["flashcards"]
        latest_quiz = study_material["quiz"]

    except Exception as e:

        print(e)

        latest_summary = "Unable to generate summary."
        latest_flashcards = []
        latest_quiz = []

    return render_template(
        "result.html",
        filename=pdf.filename,
        extracted_text=text,
        summary=latest_summary,
        flashcards=latest_flashcards,
        quiz=latest_quiz
    )


@app.route("/download-pdf")
def download_pdf():

    pdf = generate_pdf(
        latest_summary,
        latest_flashcards,
        latest_quiz
    )

    return send_file(
        BytesIO(pdf),
        as_attachment=True,
        download_name="AcademIx_Study_Material.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)