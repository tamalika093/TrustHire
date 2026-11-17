
from pydantic import BaseModel, Field


class OfferRequest(BaseModel):
    offer_text: str = Field(
        ...,
        min_length=10,
        description="The job or internship offer text to analyse"
    )
