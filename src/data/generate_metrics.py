import numpy as np
import pandas as pd


def generate_metrics(samples: int = 1000, seed: int = 42) -> pd.DataFrame:
    """Generate synthetic infrastructure metrics for the AIOps pipeline."""

    rng = np.random.default_rng(seed)

    timestamps = pd.date_range(
        start="2026-01-01",
        periods=samples,
        freq="min"
    )

    cpu = rng.normal(45, 8, samples)
    memory = rng.normal(55, 7, samples)
    disk = rng.normal(50, 5, samples)
    network = rng.normal(100, 15, samples)
    request_rate = rng.normal(200, 30, samples)

    # Inject abnormal periods to simulate incidents.
    anomaly_indices = rng.choice(samples, size=30, replace=False)

    cpu[anomaly_indices] += rng.uniform(30, 50, len(anomaly_indices))
    memory[anomaly_indices] += rng.uniform(20, 35, len(anomaly_indices))
    network[anomaly_indices] += rng.uniform(50, 100, len(anomaly_indices))

    data = pd.DataFrame(
        {
            "timestamp": timestamps,
            "cpu_usage": np.clip(cpu, 0, 100),
            "memory_usage": np.clip(memory, 0, 100),
            "disk_usage": np.clip(disk, 0, 100),
            "network_traffic": np.maximum(network, 0),
            "request_rate": np.maximum(request_rate, 0),
            "known_anomaly": False,
        }
    )

    data.loc[anomaly_indices, "known_anomaly"] = True

    return data



if __name__ == "__main__":
    metrics = generate_metrics()

    output_path = "data/raw/metrics.csv"
    metrics.to_csv(output_path, index=False)

    print(f"Generated {len(metrics)} metric records.")
    print(f"Saved to: {output_path}")