from data.generate_metrics import generate_metrics
from anomaly_detection.isolation_forest import detect_anomalies
from prediction.train_lstm import main as train_lstm
from monitoring.incident_risk import calculate_incident_risk
from remediation.auto_remediation import run_remediation


def run_pipeline():
    print("=" * 60)
    print("AIOps Monitoring System")
    print("=" * 60)

    print("\n[1/5] Generating infrastructure metrics...")
    generate_metrics()

    print("\n[2/5] Running anomaly detection...")
    detect_anomalies()

    print("\n[3/5] Training LSTM prediction model...")
    train_lstm()

    print("\n[4/5] Calculating incident risk...")
    calculate_incident_risk()

    print("\n[5/5] Running remediation analysis...")
    run_remediation()

    print("\n" + "=" * 60)
    print("AIOps pipeline completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
