import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from tensorflow.keras.models import load_model


FEATURES = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "network_traffic",
    "request_rate",
]

SEQUENCE_LENGTH = 20


def main():
    # Load data
    data = pd.read_csv("data/raw/metrics.csv")

    values = data[FEATURES].values

    # Scale the data in the same way as training.
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(values)

    # Create sequences.
    X = []
    y = []

    for i in range(SEQUENCE_LENGTH, len(scaled)):
        X.append(scaled[i - SEQUENCE_LENGTH:i])
        y.append(scaled[i])

    X = np.array(X)
    y = np.array(y)

    # Use the same final 20% as our test set.
    split_index = int(len(X) * 0.8)

    X_test = X[split_index:]
    y_test = y[split_index:]

    # Load trained model.
    model = load_model("models/lstm_incident_predictor.keras")

    # Generate predictions.
    predictions = model.predict(X_test, verbose=0)

    # Calculate overall error.
    mae = mean_absolute_error(
        y_test.flatten(),
        predictions.flatten(),
    )

    print(f"Test MAE: {mae:.6f}")

    # Plot CPU prediction vs actual.
    plt.figure(figsize=(14, 6))

    plt.plot(
        y_test[:, 0],
        label="Actual CPU",
        color="steelblue",
    )

    plt.plot(
        predictions[:, 0],
        label="Predicted CPU",
        color="orange",
    )

    plt.title("LSTM Infrastructure Metric Prediction")
    plt.xlabel("Test Time Step")
    plt.ylabel("Scaled CPU Usage")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    output_path = "data/processed/lstm_predictions.png"
    plt.savefig(output_path, dpi=150)
    plt.close()

    print(f"Prediction plot saved to: {output_path}")


if __name__ == "__main__":
    main()
