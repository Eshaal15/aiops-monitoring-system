import os

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


FEATURES = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "network_traffic",
    "request_rate",
]

SEQUENCE_LENGTH = 20


def load_data(input_path="data/raw/metrics.csv"):
    data = pd.read_csv(input_path)

    values = data[FEATURES].values

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(values)

    X = []
    y = []

    for i in range(SEQUENCE_LENGTH, len(scaled)):
        X.append(scaled[i - SEQUENCE_LENGTH:i])
        y.append(scaled[i])

    return np.array(X), np.array(y)


def build_model(input_shape):
    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),

        LSTM(32),
        Dropout(0.2),

        Dense(32, activation="relu"),
        Dense(len(FEATURES)),
    ])

    model.compile(
        optimizer="adam",
        loss="mse",
        metrics=["mae"],
    )

    return model


def main():
    X, y = load_data()

    # Keep the time ordering intact.
    split_index = int(len(X) * 0.8)

    X_train = X[:split_index]
    y_train = y[:split_index]

    X_test = X[split_index:]
    y_test = y[split_index:]

    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    model = build_model(
        input_shape=(X_train.shape[1], X_train.shape[2])
    )

    early_stopping = EarlyStopping(
        monitor="val_loss",
        patience=5,
        restore_best_weights=True,
    )

    history = model.fit(
        X_train,
        y_train,
        validation_split=0.2,
        epochs=30,
        batch_size=32,
        callbacks=[early_stopping],
        verbose=1,
    )

    os.makedirs("models", exist_ok=True)

    model.save("models/lstm_incident_predictor.keras")

    print("\nTraining complete.")
    print("Model saved to: models/lstm_incident_predictor.keras")

    test_loss, test_mae = model.evaluate(
        X_test,
        y_test,
        verbose=0,
    )

    print(f"Test loss: {test_loss:.6f}")
    print(f"Test MAE: {test_mae:.6f}")


if __name__ == "__main__":
    main()
