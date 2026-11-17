from fastapi import APIRouter

from app.schemas.offer import OfferRequest
from app.services.ai_service import analyze_job_offer
from app.services.gemini_service import analyze_offer_with_gemini

router = APIRouter(
    prefix="/api/analyze",
    tags=["Offer Analysis"]
)


@router.post("/offer")
def analyze_offer(request: OfferRequest):

    # Step 1: Run our backup keyword-based analysis
    result = analyze_job_offer(request.offer_text)

    # Step 2: Try to get Gemini AI analysis
    gemini_result = analyze_offer_with_gemini(request.offer_text)

    # Step 3: Add Gemini's result to the response
    result["gemini_analysis"] = gemini_result

    if gemini_result:
        result["ai_status"] = "Gemini analysis successful"
    else:
        result["ai_status"] = "Keyword-based fallback used"

    return result