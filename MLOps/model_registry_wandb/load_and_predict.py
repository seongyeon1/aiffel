# load_and_predict.py
import os
import pandas as pd
import psycopg2
# from sklearn.pipeline import Pipeline

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import SVC
import joblib
import wandb

# 0. set wandb environments
wandb.init(project="sklearn", entity="seongyeonkim")

# 1. download model from wandb
model_path = "sk_model.joblib"
wandb.restore(model_path)

# 2. load the model
model_pipeline = joblib.load(model_path)

# 3. get new data for prediction
db_connect = psycopg2.connect(
    user="myuser",
    password="mypassword",
    host="localhost",
    port=5432,
    database="mydatabase",
)

db_connect = psycopg2.connect(
    user="myuser",
    password="mypassword",
    host="localhost",
    port=5432,
    database="mydatabase",
)

df = pd.read_sql("SELECT * FROM iris_data ORDER BY id DESC LIMIT 100", db_connect)

X = df.drop(["id", "timestamp", "target"], axis="columns")
y = df["target"]
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, random_state=2022)

# 2. model development and train
model_pipeline.fit(X_train, y_train)

train_pred = model_pipeline.predict(X_train)
valid_pred = model_pipeline.predict(X_valid)

train_acc = accuracy_score(y_true=y_train, y_pred=train_pred)
valid_acc = accuracy_score(y_true=y_valid, y_pred=valid_pred)

print("Train Accuracy :", train_acc)
print("Valid Accuracy :", valid_acc)

# Finish the wandb run
wandb.finish()
