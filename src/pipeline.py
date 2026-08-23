import logging
from pathlib import Path

from data.generate_metrics import generate_metrics
from anomaly_detection.isolation_forest import detect_anomalies
from monitoring.incident_risk import calculate_incident_risk
from remediation.auto_remediation import run_remediation


LOG_DIR = Path("data/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "aiops.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def run_pipeline():
    logger.info("AIOps pipeline started.")

    print("=" * 60)
    print("AIOps Monitoring System")
    print("=" * 60)

    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    Path("models").mkdir(parents=True, exist_ok=True)

    print("\n[1/4] Generating infrastructure metrics...")
    logger.info("Generating infrastructure metrics.")

    metrics = generate_metrics()
    metrics.to_csv("data/raw/metrics.csv", index=False)

    logger.info(
        "Generated %d infrastructure metric records.",
        len(metrics),
    )

    print(f"Generated {len(metrics)} metric records.")
    print("Saved to: data/raw/metrics.csv")

    print("\n[2/4] Running anomaly detection...")
    logger.info("Starting anomaly detection.")

    anomalies = detect_anomalies()

    anomaly_count = int(anomalies["is_anomaly"].sum())

    logger.info(
        "Anomaly detection completed. Detected %d anomalies.",
        anomaly_count,
    )

    print("\n[3/4] Calculating incident risk...")
    logger.info("Starting incident risk calculation.")

    calculate_incident_risk()

    logger.info("Incident risk calculation completed.")

    print("\n[4/4] Running remediation analysis...")
    logger.info("Starting remediation analysis.")

    run_remediation()

    logger.info("Remediation analysis completed.")
    logger.info("AIOps pipeline completed successfully.")

    print("\n" + "=" * 60)
    print("AIOps pipeline completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
