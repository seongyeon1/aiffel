import streamlit as st
import requests
from pydantic import BaseModel
from typing import Dict

# Define the schema for the input data
class PredictIn(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Function to call the FastAPI backend
def predict(data: Dict):
    response = requests.post("http://api-with-model:8000/predict", json=data)
    return response.json()

# Streamlit interface
st.title("Iris Species Predictor")

sepal_length = st.number_input("Sepal Length", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input("Sepal Width", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal Length", min_value=0.0, max_value=10.0, value=1.3)
petal_width = st.number_input("Petal Width", min_value=0.0, max_value=10.0, value=0.2)

if st.button("Predict"):
    input_data = PredictIn(
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width
    )
    result = predict(input_data.dict())
    st.write(f"The predicted iris species is: {result['iris_class']}")
