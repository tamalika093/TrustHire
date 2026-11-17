from pydantic import BaseModel, Field


class URLRequest(BaseModel):
    url: str = Field(
        ...,
        min_length=3,
        max_length=2048,
        description="The website URL to analyse for possible phishing risks"
    )