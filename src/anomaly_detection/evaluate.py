import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix


def evaluate_detector(
    input_path: str = "data/processed/anomalies.csv",
) -> None:
    data = pd.read_csv(input_path)

    y_true = data["known_anomaly"]
    y_pred = data["is_anomaly"]

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

    print("\nClassification Report:")
    print(
        classification_report(
            y_true,
            y_pred,
            target_names=["Normal", "Anomaly"],
            zero_division=0,
        )
    )


if __name__ == "__main__":
    evaluate_detector()