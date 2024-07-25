from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import load_model

def lstm_model(vocab_size, embedding_dim, optimizer='rmsprop'):
    model = Sequential([
        Embedding(vocab_size, embedding_dim),
        LSTM(128),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['acc'])
    return model