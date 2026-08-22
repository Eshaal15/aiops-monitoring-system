import os
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


def restart_kubernetes_deployment():
    """Restart the AIOps Kubernetes deployment."""
    from kubernetes import client, config

    try:
        config.load_incluster_config()
    except Exception:
        config.load_kube_config()

    apps_api = client.AppsV1Api()

    deployment = apps_api.read_namespaced_deployment(
        name="aiops-app",
        namespace="default",
    )

    annotations = deployment.spec.template.metadata.annotations or {}
    annotations["aiops/restarted-at"] = datetime.utcnow().isoformat()

    deployment.spec.template.metadata.annotations = annotations

    apps_api.patch_namespaced_deployment(
        name="aiops-app",
        namespace="default",
        body=deployment,
    )

    return "EXECUTED"


def run_remediation(
    input_path=INPUT_PATH,
    output_path=OUTPUT_PATH,
):
    data = pd.read_csv(input_path)

    data["recommended_action"] = data.apply(
        determine_action,
        axis=1,
    )

    execution_mode = os.getenv("AIOPS_REMEDIATION_MODE", "DRY_RUN")

    statuses = []

    for action in data["recommended_action"]:
        if action == "no_action":
            statuses.append("NOT_REQUIRED")
        elif execution_mode == "KUBERNETES":
            if action == "restart_application":
                try:
                    statuses.append(restart_kubernetes_deployment())
                except Exception as exc:
                    print(f"Kubernetes remediation failed: {exc}")
                    statuses.append("FAILED")
            else:
                statuses.append("MONITORING")
        else:
            statuses.append("SIMULATED")

    data["execution_mode"] = execution_mode
    data["action_status"] = statuses
    data["action_timestamp"] = datetime.utcnow().isoformat()

    data.to_csv(output_path, index=False)

    print("AIOps remediation analysis completed.")
    print(f"Execution mode: {execution_mode}")
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