import pandas as pd
from sklearn.ensemble import IsolationForest


FEATURES = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "network_traffic",
    "request_rate",
]


def detect_anomalies(
    input_path: str = "data/raw/metrics.csv",
    output_path: str = "data/processed/anomalies.csv",
) -> pd.DataFrame:
    """Detect anomalous infrastructure behavior using Isolation Forest."""

    data = pd.read_csv(input_path)

    model = IsolationForest(
    n_estimators=200,
    contamination=0.03,
    random_state=42,
)

# Train the model on the infrastructure metrics.
    model.fit(data[FEATURES])

# Calculate anomaly scores and predictions.
    data["anomaly_score"] = model.decision_function(data[FEATURES])
    data["anomaly"] = model.predict(data[FEATURES])

    # Isolation Forest returns:
    #   1  = normal
    #  -1  = anomaly
    data["is_anomaly"] = data["anomaly"] == -1

    data.to_csv(output_path, index=False)

    anomaly_count = data["is_anomaly"].sum()

    print(f"Processed {len(data)} records.")
    print(f"Detected {anomaly_count} anomalies.")
    print(f"Saved results to: {output_path}")

    return data


if __name__ == "__main__":
    detect_anomalies()
