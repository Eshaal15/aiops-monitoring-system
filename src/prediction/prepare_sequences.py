import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


FEATURES = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "network_traffic",
    "request_rate",
]


def create_sequences(
    input_path: str = "data/raw/metrics.csv",
    sequence_length: int = 20,
):
    """Prepare time-series sequences for an LSTM model."""

    data = pd.read_csv(input_path)

    values = data[FEATURES].values

    scaler = MinMaxScaler()
    scaled_values = scaler.fit_transform(values)

    X = []
    y = []

    for i in range(sequence_length, len(scaled_values)):
        X.append(scaled_values[i - sequence_length:i])
        y.append(scaled_values[i])

    X = np.array(X)
    y = np.array(y)

    print(f"Created {len(X)} sequences.")
    print(f"Input shape: {X.shape}")
    print(f"Target shape: {y.shape}")

    return X, y


if __name__ == "__main__":
    create_sequences()
