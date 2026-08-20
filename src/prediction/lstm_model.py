import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


def build_lstm(input_shape):
    """Build an LSTM model for infrastructure metric prediction."""

    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),

        LSTM(32),
        Dropout(0.2),

        Dense(32, activation="relu"),
        Dense(5),
    ])

    model.compile(
        optimizer="adam",
        loss="mse",
        metrics=["mae"],
    )

    return model


if __name__ == "__main__":
    model = build_lstm((20, 5))
    model.summary()
