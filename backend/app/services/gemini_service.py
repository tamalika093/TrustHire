
from google import genai

from app.core.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_offer_with_gemini(offer_text: str):

    prompt = f"""
    You are a job fraud detection assistant.

    Analyse the following job or internship offer.

    Identify:
    1. Suspicious payment requests.
    2. Fake selection promises.
    3. Requests for passwords or OTPs.
    4. Suspicious communication methods.
    5. Any other possible warning signs.

    Explain why each warning sign is suspicious.

    Do not automatically declare an offer fraudulent.
    If there is not enough evidence, say so.

    Job offer:
    {offer_text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text

    except Exception as error:
        print(f"Gemini is temporarily unavailable: {error}")
        return None
