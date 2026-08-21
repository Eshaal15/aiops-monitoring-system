from pathlib import Path

from data.generate_metrics import generate_metrics
from anomaly_detection.isolation_forest import detect_anomalies
from monitoring.incident_risk import calculate_incident_risk
from remediation.auto_remediation import run_remediation


def run_pipeline():
    print("=" * 60)
    print("AIOps Monitoring System")
    print("=" * 60)

    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    Path("models").mkdir(parents=True, exist_ok=True)

    print("\n[1/4] Generating infrastructure metrics...")
    metrics = generate_metrics()
    metrics.to_csv("data/raw/metrics.csv", index=False)
    print(f"Generated {len(metrics)} metric records.")
    print("Saved to: data/raw/metrics.csv")

    print("\n[2/4] Running anomaly detection...")
    detect_anomalies()

    print("\n[3/4] Calculating incident risk...")
    calculate_incident_risk()

    print("\n[4/4] Running remediation analysis...")
    run_remediation()

    print("\n" + "=" * 60)
    print("AIOps pipeline completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
