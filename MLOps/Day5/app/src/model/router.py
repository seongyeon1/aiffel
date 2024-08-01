from fastapi import APIRouter

import torch
from .textclassifier import model
from .schemas import TextRequest
from .schemas import SentimentResponse
from .vocabs import open_json

from kiwipiepy import Kiwi


router = APIRouter()

kiwi = Kiwi()


def preprocessing_with_kiwi(text: str) -> list[str]:
    return [t.form for t in kiwi.tokenize(text)]


stopwords: set[str] = {
    "도",
    "는",
    "다",
    "의",
    "가",
    "이",
    "은",
    "한",
    "에",
    "하",
    "고",
    "을",
    "를",
    "인",
    "듯",
    "과",
    "와",
    "네",
    "들",
    "듯",
    "지",
    "임",
    "게",
}

from pathlib import Path

index_to_tag = {0: "부정", 1: "긍정"}
file_path = Path(__file__).parent.absolute() / "naver_vocab.json"
word_to_index = open_json(file_path)


@router.post("/predict/", response_model=SentimentResponse)
async def predict_sentiment(request: TextRequest) -> SentimentResponse:
    # input text 토큰화
    tokens = preprocessing_with_kiwi(request.sentence)
    # remove stopwords
    tokens = [word for word in tokens if not word in stopwords]
    token_indices = [word_to_index.get(token, 1) for token in tokens]

    # token to tensor
    input_tensor = torch.tensor([token_indices], dtype=torch.long)

    with torch.no_grad():
        logits = model(input_tensor)

    predicted_index = torch.argmax(logits, dim=1)
    prdicted_tag = index_to_tag[predicted_index.item()]

    return SentimentResponse(lab=prdicted_tag)