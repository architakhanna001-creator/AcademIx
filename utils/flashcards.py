import re
from utils.ai import generate_response


def generate_flashcards(text):

    # Limit text size
    text = text[:12000]

    prompt = f"""
You are StudyMate AI.

Read the notes below and generate exactly 10 flashcards.

Rules:
- One question and one answer.
- Questions should be short.
- Answers should be concise.

Return ONLY in this format:

Q: Question
A: Answer

Q: Question
A: Answer

Continue until Question 10.

Notes:

{text}
"""

    response = generate_response(prompt)

    # Convert AI response into a list of dictionaries
    flashcards = []

    pattern = r"Q:\s*(.*?)\s*A:\s*(.*?)(?=\n\s*Q:|\Z)"

    matches = re.findall(pattern, response, re.DOTALL)

    for question, answer in matches:
        flashcards.append({
            "question": question.strip(),
            "answer": answer.strip()
        })

    return flashcards