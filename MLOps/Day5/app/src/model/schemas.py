from pydantic import BaseModel


class TextRequest(BaseModel):
    sentence: str


class SentimentResponse(BaseModel):
    lab: str