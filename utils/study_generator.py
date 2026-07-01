import json
import re
from utils.ai import generate_response


def generate_study_material(text):

    # Prevent extremely large prompts
    text = text[:12000]

    prompt = f"""
You are AcademIx.

Generate study material from the notes below.

IMPORTANT:
Return ONLY ONE valid JSON object.

The JSON MUST be valid and parsable using Python json.loads().

VERY IMPORTANT RULES:

1. Do NOT use markdown.
2. Do NOT wrap JSON inside ```json.
3. The summary MUST be ONE continuous paragraph.
4. Do NOT insert line breaks inside the summary.
5. Escape every quotation mark inside text using \\"
6. Do NOT include raw double quotes inside the summary, questions, answers or options.
7. Return ONLY valid JSON.

Required format:

{{
    "summary":"A detailed summary of about 450-500 words written as ONE paragraph.",

    "flashcards":[
        {{
            "question":"Question",
            "answer":"Answer"
        }}
    ],

    "quiz":[
        {{
            "question":"Question",
            "options":[
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer":"Correct Option"
        }}
    ]
}}

Rules:

- Summary: 450-500 words
- Exactly 10 flashcards
- Exactly 10 quiz questions
- Exactly 4 options per question
- The answer MUST exactly match one option.
- The "answer" must be an exact character-for-character copy of one of the options.

Notes:

{text}
"""

    response = generate_response(prompt)

    # --------------------------
    # Clean Gemini response
    # --------------------------

    response = response.strip()

    if response.startswith("```json"):
        response = response[7:]

    if response.startswith("```"):
        response = response[3:]

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    # Remove control characters
    response = response.replace("\r", "")
    response = response.replace("\t", " ")

    # --------------------------
    # Try parsing normally
    # --------------------------

    try:

        data = json.loads(response)

    except json.JSONDecodeError:

        # Gemini sometimes forgets to escape quotes like:
        # "What is "Promiscuous Mode"?"
        # Fix the most common cases.

        response = re.sub(
            r'(?<=:")([^"]*)"([^"]*)"([^"]*)(?=",)',
            lambda m: (
                m.group(1)
                + '\\"'
                + m.group(2)
                + '\\"'
                + m.group(3)
            ),
            response,
        )

        try:
            data = json.loads(response)

        except Exception as e:

            print("\n========== JSON ERROR ==========\n")
            print(e)
            print("\nGemini Response:\n")
            print(response)

            return {
                "summary": "Unable to generate summary.",
                "flashcards": [],
                "quiz": []
            }

    return {
        "summary": data.get("summary", ""),
        "flashcards": data.get("flashcards", []),
        "quiz": data.get("quiz", [])
    }