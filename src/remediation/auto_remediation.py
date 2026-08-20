import pandas as pd
from datetime import datetime


INPUT_PATH = "data/processed/incident_risk.csv"
OUTPUT_PATH = "data/processed/remediation_actions.csv"


def determine_action(row):
    """Determine a safe remediation action from incident risk."""

    if row["risk_level"] == "HIGH":
        return "restart_application"

    if row["risk_level"] == "MEDIUM":
        return "increase_monitoring"

    return "no_action"


def run_remediation(
    input_path=INPUT_PATH,
    output_path=OUTPUT_PATH,
):
    data = pd.read_csv(input_path)

    data["recommended_action"] = data.apply(
        determine_action,
        axis=1,
    )

    # Dry-run mode:
    # We record what the system WOULD do without
    # changing any real infrastructure.
    data["execution_mode"] = "DRY_RUN"

    data["action_status"] = data["recommended_action"].apply(
        lambda action: (
            "SIMULATED"
            if action != "no_action"
            else "NOT_REQUIRED"
        )
    )

    data["action_timestamp"] = datetime.utcnow().isoformat()

    data.to_csv(output_path, index=False)

    print("AIOps remediation analysis completed.")
    print(f"Total observations: {len(data)}")
    print(
        "Restart actions:",
        (data["recommended_action"] == "restart_application").sum(),
    )
    print(
        "Monitoring actions:",
        (data["recommended_action"] == "increase_monitoring").sum(),
    )
    print(
        "No-action observations:",
        (data["recommended_action"] == "no_action").sum(),
    )
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    run_remediation()
