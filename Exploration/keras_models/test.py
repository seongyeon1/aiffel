import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import os


# MNIST 데이터셋 로드 및 전처리
def load_mnist_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(-1, 28 * 28) / 255.0
    x_test = x_test.reshape(-1, 28 * 28) / 255.
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    return x_train, y_train, x_test, y_test


# 모델 생성 함수

def create_model(layer_widths):
    model = Sequential()
    model.add(Dense(layer_widths[0], activation='relu', input_shape=(784,)))
    for width in layer_widths[1:]:
        model.add(Dense(width, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# 학습 및 평가 함수
def train_model(model, x_train, y_train, x_test, y_test, epochs=10):
    history = model.fit(x_train, y_train, epochs=epochs, validation_data=(x_test, y_test), verbose=2)
    return history


# 학습 및 검증 정확도를 그래프로 시각화
def plot_and_save_history(histories, titles, filename='model_comparison.png'):
    plt.figure(figsize=(12, 6))
    for history, title in zip(histories, titles):
        plt.plot(history.history['val_accuracy'], label=f'{title} val_accuracy')
        plt.plot(history.history['accuracy'], label=f'{title} accuracy')
    plt.title('Model accuracy comparison')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend(loc='lower right')
    plt.savefig(filename)
    plt.show()


def main():
    x_train, y_train, x_test, y_test = load_mnist_data()
    # 모델 정의
    basic_model = create_model([128, 64])
    wide_model = create_model([512, 256])
    narrow_model = create_model([32, 16])
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