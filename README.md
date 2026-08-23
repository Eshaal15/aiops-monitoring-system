# Intelligent AIOps Monitoring System

An AI-driven IT operations monitoring system that combines machine learning, observability, containerization, and Kubernetes to detect infrastructure anomalies, estimate incident risk, and generate automated remediation decisions.

## Overview

The system processes infrastructure metrics through an end-to-end AIOps pipeline:

```text
Infrastructure Metrics
        ↓
Isolation Forest Anomaly Detection
        ↓
LSTM Time-Series Prediction
        ↓
Incident Risk Scoring
        ↓
LOW / MEDIUM / HIGH Risk
        ↓
Remediation Decision
        ↓
DRY_RUN Action
```

The project demonstrates how machine learning can be integrated with modern monitoring and cloud-native technologies for intelligent IT operations.

## Key Features

- Infrastructure metric generation and processing
- Isolation Forest anomaly detection
- LSTM-based infrastructure time-series prediction
- Heuristic incident-risk scoring
- LOW / MEDIUM / HIGH risk classification
- Prometheus metrics exporter
- Grafana monitoring dashboards
- ELK Stack integration
- Docker and Docker Compose
- Kubernetes deployment
- Automated remediation decision layer
- DRY_RUN remediation mode for safe testing

## Machine Learning

### Isolation Forest

The anomaly detection component analyzes infrastructure features including:

- CPU usage
- Memory usage
- Disk usage
- Network traffic
- Request rate

A representative pipeline run generated **1,000 metric records** and detected **30 anomalies**.

### LSTM

The LSTM model is used for infrastructure time-series prediction and contributes prediction risk to the incident-risk engine.

Model architecture:

```text
LSTM(64)
    ↓
Dropout
    ↓
LSTM(32)
    ↓
Dropout
    ↓
Dense(32)
    ↓
Dense(5)
```

The model is used as part of the incident-risk scoring system.

## Incident Risk

Incident risk combines:

- Anomaly signal: **60%**
- LSTM prediction risk: **40%**

Risk thresholds:

| Risk Level | Score |
|------------|-------|
| HIGH | >= 0.75 |
| MEDIUM | >= 0.40 |
| LOW | < 0.40 |

The risk engine uses these thresholds to classify infrastructure observations and determine the appropriate remediation response.

## Remediation

The remediation layer converts risk decisions into recommended actions.

Current actions include:

- `no_action`
- `restart_application`

Remediation currently runs in `DRY_RUN` mode.

This means the system generates and records remediation decisions without actually restarting production infrastructure.

A representative pipeline run generated:

- **950** `no_action` decisions
- **30** `restart_application` decisions

## Observability

### Prometheus

The application exposes monitoring metrics including:

- `aiops_cpu_usage_percent`
- `aiops_memory_usage_percent`
- `aiops_anomalies_detected_total`
- `aiops_remediation_actions_total`

### Grafana

Grafana provides visualization of the monitoring metrics collected by Prometheus.

### ELK Stack

Application logs are processed through:

```text
AIOps Application
       ↓
   Logstash
       ↓
 Elasticsearch
       ↓
    Kibana
```

Kibana can be used to explore AIOps log data and visualize log activity by service and timestamp.

## Containerization

The project includes Docker and Docker Compose configurations for the AIOps application and monitoring stack.

Services include:

- AIOps application
- Prometheus
- Grafana
- Elasticsearch
- Logstash
- Kibana

Start the complete monitoring stack with:

```bash
docker compose up -d
```

Check the running containers with:

```bash
docker compose ps
```

## Kubernetes

The AIOps application is packaged as a Kubernetes Deployment with an associated Service.

The Kubernetes configuration is located in:

```text
k8s/
└── aiops-app.yaml
```

The Kubernetes environment can be used to deploy and verify the containerized AIOps application and its pipeline.

## Project Structure

```text
aiops-monitoring-system/
├── data/
│   ├── raw/
│   ├── processed/
│   └── logs/
├── models/
├── src/
│   ├── data/
│   ├── anomaly_detection/
│   ├── prediction/
│   ├── monitoring/
│   └── remediation/
├── monitoring/
│   ├── prometheus/
│   └── logstash/
├── k8s/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── start.py
├── requirements.txt
└── README.md
```

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow / Keras
- ONNX Runtime
- Prometheus
- Grafana
- Elasticsearch
- Logstash
- Kibana
- Docker
- Docker Compose
- Kubernetes
- Git
- GitHub

## Purpose

This project demonstrates practical experience across:

- Artificial Intelligence
- Machine Learning
- AIOps
- Observability
- MLOps concepts
- Containerization
- Kubernetes
- Monitoring
- Log analytics
- Automation
- Cloud engineering concepts

## Author

**Eshaal**

GitHub: **Eshaal15**
