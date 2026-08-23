import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model


FEATURES = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "network_traffic",
    "request_rate",
]

SEQUENCE_LENGTH = 20


def calculate_incident_risk(
    metrics_path="data/raw/metrics.csv",
    anomalies_path="data/processed/anomalies.csv",
    model_path="models/lstm_incident_predictor.keras",
    output_path="data/processed/incident_risk.csv",
):
    # Load metric data and anomaly results.
    metrics = pd.read_csv(metrics_path)
    anomalies = pd.read_csv(anomalies_path)

    # Load the trained LSTM model.
    model = load_model(model_path)

    values = metrics[FEATURES].values

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(values)

    # Prepare LSTM sequences.
    X = []

    for i in range(SEQUENCE_LENGTH, len(scaled)):
        X.append(scaled[i - SEQUENCE_LENGTH:i])

    X = np.array(X, dtype=np.float32)

    # Run LSTM inference.
    predictions = model.predict(X, verbose=0)

    # Prediction error indicates how unexpected the next observation is.
    actual = scaled[SEQUENCE_LENGTH:]

    prediction_error = np.mean(
        np.abs(actual - predictions),
        axis=1,
    )

    # Normalize prediction error to 0-1.
    error_min = prediction_error.min()
    error_max = prediction_error.max()

    if error_max > error_min:
        prediction_risk = (
            (prediction_error - error_min)
            / (error_max - error_min)
        )
    else:
        prediction_risk = np.zeros_like(prediction_error)

    # Align Isolation Forest results with LSTM predictions.
    anomaly_signal = anomalies["is_anomaly"].iloc[
        SEQUENCE_LENGTH:
    ].astype(float).values

    # Combine anomaly detection and LSTM prediction signals.
    risk_score = (
        0.6 * anomaly_signal
        + 0.4 * prediction_risk
    )

    result = metrics.iloc[SEQUENCE_LENGTH:].copy()

    result["anomaly_signal"] = anomaly_signal
    result["prediction_risk"] = prediction_risk
    result["incident_risk"] = risk_score

    result["risk_level"] = np.select(
        [
            result["incident_risk"] >= 0.75,
            result["incident_risk"] >= 0.40,
        ],
        [
            "HIGH",
            "MEDIUM",
        ],
        default="LOW",
    )

    result.to_csv(output_path, index=False)

    print(f"Processed {len(result)} observations.")
    print(
        "High-risk incidents:",
        (result["risk_level"] == "HIGH").sum(),
    )
    print(
        "Medium-risk incidents:",
        (result["risk_level"] == "MEDIUM").sum(),
    )
    print(
        "Low-risk observations:",
        (result["risk_level"] == "LOW").sum(),
    )
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    calculate_incident_risk()
