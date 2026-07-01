from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)


def add_page_number(canvas, doc):
    canvas.saveState()

    canvas.setFont("Helvetica", 9)

    canvas.drawRightString(
        7.6 * inch,
        0.5 * inch,
        f"Page {doc.page}"
    )

    canvas.restoreState()


def generate_pdf(summary, flashcards, quiz):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    title = styles["Title"]
    title.alignment = TA_CENTER
    title.textColor = colors.HexColor("#404E3B")

    heading = styles["Heading1"]
    heading.textColor = colors.HexColor("#6C8480")

    body = styles["BodyText"]
    body.leading = 22
    body.spaceAfter = 10

    story = []

    # ----------------------------------------------------
    # Title
    # ----------------------------------------------------

    story.append(Paragraph("✦ AcademIx", title))
    story.append(
        Paragraph(
            "<b>AI Powered Study Material</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            datetime.now().strftime(
                "Generated on %d %B %Y, %I:%M %p"
            ),
            styles["Italic"]
        )
    )

    story.append(Spacer(1, 18))

    story.append(HRFlowable(
        width="100%",
        thickness=1.2,
        color=colors.HexColor("#BAC8B1")
    ))

    story.append(Spacer(1, 20))

    # ----------------------------------------------------
    # Summary
    # ----------------------------------------------------

    story.append(Paragraph("📝 Summary", heading))
    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            summary.replace("\n", "<br/>"),
            body
        )
    )

    story.append(Spacer(1, 18))

    story.append(HRFlowable(
        width="100%",
        thickness=1,
        color=colors.HexColor("#BAC8B1")
    ))

    story.append(Spacer(1, 18))

    # ----------------------------------------------------
    # Flashcards
    # ----------------------------------------------------

    story.append(Paragraph("🧠 Flashcards", heading))
    story.append(Spacer(1, 12))

    for i, card in enumerate(flashcards, start=1):

        story.append(
            Paragraph(
                f"<b>Flashcard {i}</b>",
                styles["Heading3"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Question:</b> {card['question']}",
                body
            )
        )

        story.append(
            Paragraph(
                f"<b>Answer:</b> {card['answer']}",
                body
            )
        )

        story.append(Spacer(1, 12))

    story.append(HRFlowable(
        width="100%",
        thickness=1,
        color=colors.lightgrey
    ))

    story.append(Spacer(1, 18))

    # ----------------------------------------------------
    # Quiz
    # ----------------------------------------------------

    story.append(Paragraph("❓ Practice Quiz", heading))
    story.append(Spacer(1, 12))

    for i, q in enumerate(quiz, start=1):

        story.append(
            Paragraph(
                f"<b>Question {i}</b>",
                styles["Heading3"]
            )
        )

        story.append(
            Paragraph(
                q["question"],
                body
            )
        )

        letters = ["A", "B", "C", "D"]

        for letter, option in zip(letters, q["options"]):

            story.append(
                Paragraph(
                    f"{letter}. {option}",
                    body
                )
            )

        story.append(
            Paragraph(
                f"<font color='#404E3B'><b>Correct Answer:</b> {q['answer']}</font>",
                body
            )
        )

        story.append(Spacer(1, 14))

    doc.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

    pdf = buffer.getvalue()

    buffer.close()

    return pdf