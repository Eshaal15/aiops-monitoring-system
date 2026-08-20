import subprocess
import sys
import time

metrics = subprocess.Popen(
    [sys.executable, "src/monitoring/prometheus_metrics.py"]
)

try:
    pipeline = subprocess.run(
        [sys.executable, "src/pipeline.py"]
    )

    print(f"Pipeline exited with code: {pipeline.returncode}")
    print("Prometheus metrics server will continue running.")

    while True:
        time.sleep(60)

except KeyboardInterrupt:
    metrics.terminate()
    sys.exit(0)
