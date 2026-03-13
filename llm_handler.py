import os
from google import genai

# Initialize client once
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_ai(question, profile=None):
    """
    Ask Google Gemini AI with optional profile controlling response style.
    profile: dict, e.g. {"response_style": "simple" or "detailed"}
    """
    try:
        # Build prompt based on profile
        if profile:
            style = profile.get("response_style", "")
            if style == "simple":
                prompt = f"Explain in very simple and short sentences: {question}"
            elif style == "detailed":
                prompt = f"Explain clearly in detail: {question}"
            else:
                prompt = question
        else:
            prompt = question

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()

    except Exception:
        return "I am having trouble connecting to the AI service."