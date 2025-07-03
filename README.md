# 🥭 Macadamia Construction Analytics Pipeline

[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat&logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=flat&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)

**Automated ETL pipeline for construction cost analysis** mirroring professional workflows at Macadamia Homebuilders. Processes cost and material data using PySpark, stores results in SQLite and AWS S3, with Dockerized execution.

## 🔍 Project Overview
This solution replicates my work at Macadamia Homebuilders where I:
- Automated 50+ monthly cost/material reports
- Reduced manual effort by 70%
- Enabled real-time Power BI dashboards

## 🚀 Features
- **PySpark ETL**: Scalable data processing
- **Cost Variance Analysis**: Actual vs Planned costs
- **Material Usage Tracking**: Quantity and location aggregation
- **Cloud Integration**: AWS S3 storage (Parquet format)
- **SQLite Database**: Power BI-ready datasets
- **Dockerized Environment**: Reproducible execution

## ⚙️ Tech Stack
- **Core**: Python, PySpark, Pandas, SQLAlchemy
- **Infrastructure**: Docker, Docker Compose
- **Storage**: SQLite (local), AWS S3 (cloud)
- **Analytics**: Power BI (via SQLite/S3)

## 🛠️ Setup & Execution

### Prerequisites
- Docker Desktop
- AWS Account (for S3 - optional)

### Installation
```bash
# Clone repository
git clone https://github.com/rgb101593/macadamia-data-pipeline.git
cd macadamia-data-pipeline

# Build Docker image
docker-compose build

# Run pipeline
docker-compose up