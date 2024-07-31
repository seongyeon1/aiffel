FROM --platform=linux/arm64 python:3.9-slim

WORKDIR /usr/app

RUN pip install -U pip &&\
    pip install mlflow==1.30.0 pandas scikit-learn "fastapi[all]"

COPY schemas.py schemas.py
COPY app.py app.py
COPY sk_model/ sk_model/

# Expose the FastAPI port
EXPOSE 8000 # streamlit이 사용해야함

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
