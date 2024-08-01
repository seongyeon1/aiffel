import torch
import torch.nn as nn
import torch.nn.functional as F
from .vocabs import open_json

from pathlib import Path

file_path = Path(__file__).parent.absolute() / "naver_vocab.json"
word_to_index = open_json(file_path)


class TextClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(TextClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # x: (batch_size, seq_length)
        embedded = self.embedding(x)  # (batch_size, seq_length, embedding_dim)

        # LSTM은 (hidden state, cell state)의 튜플을 반환합니다
        lstm_out, (hidden, cell) = self.lstm(
            embedded
        )  # lstm_out: (batch_size, seq_length, hidden_dim), hidden: (1, batch_size, hidden_dim)

        last_hidden = hidden.squeeze(0)  # (batch_size, hidden_dim)
        logits = self.fc(last_hidden)  # (batch_size, output_dim)
        return logits


model = TextClassifier(
    vocab_size=len(word_to_index), embedding_dim=100, hidden_dim=128, output_dim=2
)
model.load_state_dict(
    torch.load(
        Path(__file__).parent.absolute() / "artifacts/best_model_checkpoint.pth",
        map_location=torch.device("cpu"),
    )
)
model.eval()