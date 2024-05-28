import tensorflow as tf

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

import os


# MNIST 데이터셋 로드 및 전처리
def load_mnist_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    return x_train, y_train, x_test, y_test


# 모델 생성 함수
def create_cnn_model(conv_filters, dense_units):
    model = Sequential()
    model.add(Conv2D(conv_filters[0], kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(conv_filters[1], kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(dense_units, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# 학습 및 평가 함수

def train_model(model, x_train, y_train, x_test, y_test, epochs=10):
    history = model.fit(x_train, y_train, epochs=epochs, validation_data=(x_test, y_test), verbose=2)
    return history


# 학습 및 검증 정확도와 손실 값을 그래프로 시각화 및 저장
def plot_and_save_history(histories, titles, filename_prefix='cnn_model'):
    fig, axs = plt.subplots(2, 1, figsize=(12, 12))

    for history, title in zip(histories, titles):
        axs[0].plot(history.history['val_accuracy'], label=f'{title} val_accuracy')
        axs[0].plot(history.history['accuracy'], label=f'{title} accuracy')
        axs[1].plot(history.history['val_loss'], label=f'{title} val_loss')
        axs[1].plot(history.history['loss'], label=f'{title} loss')
    axs[0].set_title('Model Accuracy Comparison')
    axs[0].set_xlabel('Epoch')
    axs[0].set_ylabel('Accuracy')
    axs[0].legend(loc='lower right')
    axs[1].set_title('Model Loss Comparison')
    axs[1].set_xlabel('Epoch')
    axs[1].set_ylabel('Loss')
    axs[1].legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(f'{filename_prefix}_comparison.png')
    plt.show()


def main():
    x_train, y_train, x_test, y_test = load_mnist_data()
    # 모델 정의
    basic_model = create_cnn_model([32, 64], 128)
    wide_model = create_cnn_model([128, 256], 512)
    narrow_model = create_cnn_model([16, 32], 64)

    # 학습 및 성능 비교
    print("Training basic model...")
    basic_history = train_model(basic_model, x_train, y_train, x_test, y_test)
    print("Training wide model...")
    wide_history = train_model(wide_model, x_train, y_train, x_test, y_test)
    print("Training narrow model...")
    narrow_history = train_model(narrow_model, x_train, y_train, x_test, y_test)

    # 성능 비교 그래프 저장
    plot_and_save_history([basic_history, wide_history, narrow_history],
                          ['Basic Model', 'Wide Model', 'Narrow Model'])

    print("\nPerformance Comparison:")
    basic_loss, basic_accuracy = basic_model.evaluate(x_test, y_test, verbose=2)
    wide_loss, wide_accuracy = wide_model.evaluate(x_test, y_test, verbose=2)
    narrow_loss, narrow_accuracy = narrow_model.evaluate(x_test, y_test, verbose=2)

    print(f"Basic Model - Test Loss: {basic_loss}, Test Accuracy: {basic_accuracy}")
    print(f"Wide Model - Test Loss: {wide_loss}, Test Accuracy: {wide_accuracy}")
    print(f"Narrow Model - Test Loss: {narrow_loss}, Test Accuracy: {narrow_accuracy}")


if __name__ == "__main__":
    main()