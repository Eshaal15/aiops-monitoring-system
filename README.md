\# Intelligent AIOps Monitoring System



An AI-driven IT operations monitoring prototype that combines machine learning, observability, containerization, and Kubernetes to detect infrastructure anomalies, estimate incident risk, and generate automated remediation decisions.



\## Overview



The system processes infrastructure metrics through an end-to-end AIOps pipeline:



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

DRY\_RUN Action



The project demonstrates how machine learning can be integrated with modern monitoring and cloud-native technologies for intelligent IT operations.



\## Key Features



\- Infrastructure metric generation and processing

\- Isolation Forest anomaly detection

\- LSTM-based infrastructure time-series prediction

\- Heuristic incident-risk scoring

\- LOW / MEDIUM / HIGH risk classification

\- Prometheus metrics exporter

\- Grafana monitoring dashboards

\- ELK Stack integration

\- Docker and Docker Compose

\- Kubernetes deployment

\- Automated remediation decision layer

\- DRY\_RUN remediation mode for safe testing



\## Machine Learning



\### Isolation Forest



The anomaly detection component analyzes infrastructure features including:



\- CPU usage

\- Memory usage

\- Disk usage

\- Network traffic

\- Request rate



A test pipeline generated 1,000 metric records and detected 30 anomalies.



\### LSTM



The LSTM model is used for infrastructure time-series prediction and contributes prediction risk to the incident-risk engine.



Model architecture:



\- LSTM(64)

\- Dropout

\- LSTM(32)

\- Dropout

\- Dense(32)

\- Dense(5)



The model is used as part of a prototype risk-scoring system rather than being presented as a production-validated incident prediction model.



\## Incident Risk



Incident risk combines:



\- Anomaly signal: 60%

\- LSTM prediction risk: 40%



Risk thresholds:



\- HIGH: >= 0.75

\- MEDIUM: >= 0.40

\- LOW: < 0.40



These thresholds represent a prototype heuristic rather than a statistically validated probability model.



\## Remediation



The remediation layer converts risk decisions into recommended actions.



Current actions include:



\- `no\_action`

\- `restart\_application`



Remediation currently runs in `DRY\_RUN` mode.



This means the system generates and records remediation decisions without actually restarting production infrastructure.



A representative pipeline run generated:



\- 950 `no\_action` decisions

\- 30 `restart\_application` decisions



\## Observability



\### Prometheus



The application exposes monitoring metrics including:



\- `aiops\_cpu\_usage\_percent`

\- `aiops\_memory\_usage\_percent`

\- `aiops\_anomalies\_detected\_total`

\- `aiops\_remediation\_actions\_total`



\### Grafana



Grafana provides visualization of the monitoring metrics collected by Prometheus.



\### ELK Stack



Application logs are processed through:



```text

AIOps Application

&#x20;      ↓

Logstash

&#x20;      ↓

Elasticsearch

&#x20;      ↓

Kibana





Kibana can be used to explore AIOps log data and visualize log activity by service and timestamp.



Containerization

The project includes Docker and Docker Compose configurations for the AIOps application and monitoring stack.



Services include:



AIOps application

Prometheus

Grafana

Elasticsearch

Logstash

Kibana

Kubernetes

The AIOps application is packaged as a Kubernetes Deployment with an associated Service.



The Kubernetes environment was used to deploy and verify the containerized AIOps application and its pipeline.



Project Structure

aiops-monitoring-system/

├── data/

│   ├── raw/

│   ├── processed/

│   └── logs/

├── models/

├── src/

│   ├── data/

│   ├── anomaly\_detection/

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





Technologies

Python

Pandas

NumPy

Scikit-learn

TensorFlow / Keras

ONNX Runtime

Prometheus

Grafana

Elasticsearch

Logstash

Kibana

Docker

Docker Compose

Kubernetes

Git

GitHub

Current Limitations

This project is a reconstructed portfolio implementation based on the functionality described in an earlier internship project.



The following limitations are intentionally documented:



Remediation is currently DRY\_RUN and does not restart real infrastructure.

LSTM prediction contributes to a heuristic incident-risk score and has not been presented as production-validated incident prediction.

AWS deployment/integration should only be described as completed where it has been independently verified.

Purpose

This project demonstrates practical experience across:



Artificial Intelligence

Machine Learning

AIOps

Observability

MLOps concepts

Containerization

Kubernetes

Monitoring

Log analytics

Automation

Cloud engineering concepts

Author

Eshaal



GitHub: https://github.com/Eshaal15

