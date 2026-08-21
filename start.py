import subprocess
import sys
import time
from pathlib import Path

log_dir = Path("data/logs")
log_dir.mkdir(parents=True, exist_ok=True)

log_file = open(log_dir / "aiops.log", "a", buffering=1)

metrics = subprocess.Popen(
    [sys.executable, "src/monitoring/prometheus_metrics.py"],
    stdout=log_file,
    stderr=subprocess.STDOUT,
)

try:
    pipeline = subprocess.run(
        [sys.executable, "src/pipeline.py"],
        stdout=log_file,
        stderr=subprocess.STDOUT,
    )

    print(f"Pipeline exited with code: {pipeline.returncode}")
    print("Prometheus metrics server will continue running.")

    while True:
        time.sleep(60)

except KeyboardInterrupt:
    metrics.terminate()
    log_file.close()
    sys.exit(0)
