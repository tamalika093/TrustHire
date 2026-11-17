
from fastapi import APIRouter

from app.schemas.url import URLRequest
from app.services.url_service import analyze_url


router = APIRouter(
    prefix="/api/check",
    tags=["URL Safety Check"]
)


@router.post("/url")
def check_url(request: URLRequest):

    result = analyze_url(request.url)

    return result
