import json
from utils.ai import generate_response


def generate_quiz(text):

    # Prevent sending extremely large PDFs
    text = text[:12000]

    prompt = f"""
You are StudyMate AI.

Read the notes below and generate EXACTLY 10 multiple-choice questions.

Return ONLY valid JSON.

Format:

[
  {{
    "question": "Question here",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Correct Option"
  }}
]

Rules:
- Exactly 10 questions.
- Each question must have 4 options.
- The answer must exactly match one of the options.
- Do NOT write markdown.
- Do NOT write ```json.
- Return ONLY JSON.

Notes:

{text}
"""

    response = generate_response(prompt)

    try:
        return json.loads(response)

    except Exception as e:
        print("Quiz JSON Error:", e)
        print(response)
        return []