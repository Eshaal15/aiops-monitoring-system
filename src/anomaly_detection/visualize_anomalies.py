import pandas as pd
import matplotlib.pyplot as plt


def visualize_anomalies(
    input_path: str = "data/processed/anomalies.csv",
    output_path: str = "data/processed/anomaly_plot.png",
) -> None:
    """Create a visualization of detected infrastructure anomalies."""

    data = pd.read_csv(input_path)
    data["timestamp"] = pd.to_datetime(data["timestamp"])

    normal = data[~data["is_anomaly"]]
    anomalies = data[data["is_anomaly"]]

    plt.figure(figsize=(14, 6))

    plt.plot(
        normal["timestamp"],
        normal["cpu_usage"],
        label="Normal CPU Usage",
        color="steelblue",
        linewidth=1,
    )

    plt.scatter(
        anomalies["timestamp"],
        anomalies["cpu_usage"],
        label="Detected Anomaly",
        color="red",
        s=35,
        zorder=3,
    )

    plt.title("AIOps Infrastructure Anomaly Detection")
    plt.xlabel("Time")
    plt.ylabel("CPU Usage (%)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_path, dpi=150)
    plt.close()

    print(f"Visualization saved to: {output_path}")


if __name__ == "__main__":
    visualize_anomalies()
