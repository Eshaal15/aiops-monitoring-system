from prometheus_client import Gauge, Counter, start_http_server
import time
import random


CPU_USAGE = Gauge(
    "aiops_cpu_usage_percent",
    "Simulated infrastructure CPU usage",
)

MEMORY_USAGE = Gauge(
    "aiops_memory_usage_percent",
    "Simulated infrastructure memory usage",
)

ANOMALIES_DETECTED = Counter(
    "aiops_anomalies_detected_total",
    "Total number of detected anomalies",
)

REMEDIATION_ACTIONS = Counter(
    "aiops_remediation_actions_total",
    "Total number of remediation actions",
)


def start_metrics_server(port=8000):
    """Start the Prometheus metrics endpoint."""

    start_http_server(port)

    print(f"Prometheus metrics available on port {port}")

    while True:
        cpu = random.uniform(20, 90)
        memory = random.uniform(30, 85)

        CPU_USAGE.set(cpu)
        MEMORY_USAGE.set(memory)

        if cpu > 80:
            ANOMALIES_DETECTED.inc()

        if cpu > 85:
            REMEDIATION_ACTIONS.inc()

        time.sleep(5)


if __name__ == "__main__":
    start_metrics_server()
