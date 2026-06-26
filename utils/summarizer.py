from utils.ai import generate_response


def summarize_notes(text):

    # Prevent sending extremely large PDFs
    text = text[:12000]

    prompt = f"""
You are StudyMate AI, an intelligent study assistant.

Read the notes below and create study material.

Return your answer in the EXACT format below.

## 📖 Summary
Write a clear summary in 150-250 words.

## 🔑 Key Topics
List 5-10 important topics as bullet points.

## ⭐ Important Points
List the most important facts as bullet points.

## 💡 Quick Revision Tips
Give 5 short revision tips.

Notes:

{text}
"""

    return generate_response(prompt)