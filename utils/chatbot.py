from utils.ai import generate_response


def ask_doubt(notes, question):

    notes = notes[:12000]

    prompt = f"""
You are StudyMate AI.

Answer the user's question using ONLY the notes below.

If the answer is not present in the notes, clearly say:
"I couldn't find that information in the uploaded notes."

Notes:

{notes}

Question:

{question}
"""

    return generate_response(prompt)