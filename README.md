# Flask Docker Stack

A simple Flask application containerized with Docker Compose, backed by PostgreSQL and Redis, and monitored with Prometheus and Grafana.

## Overview

This project is a lightweight example of a production-style backend stack running locally in containers. It includes:

- a Flask API server
- PostgreSQL for persistence
- Redis for caching
- Prometheus for metrics scraping
- Grafana for visualization

The goal is to demonstrate how a basic API can be containerized and instrumented with observability tooling in a local development environment.

## Architecture

```text
Browser
  |
  v
Flask API (port 5000)
  |
  +--> PostgreSQL
  |
  +--> Redis
  |
  +--> Prometheus (scrapes /metrics)
         |
         v
       Grafana (port 3000)
```

## Features

- Flask API running on port 5000
- PostgreSQL database with persistent volume
- Redis service for caching and future extension
- Prometheus scraping configuration
- Grafana dashboard support
- Docker health checks
- Simple local deployment using Compose

## Tech Stack

- Python 3.11
- Flask
- PostgreSQL 15
- Redis 7
- Prometheus
- Grafana
- Docker Compose

## Repository Structure

```text
flask-docker-stack/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── prometheus.yml
├── .env
├── README.md
└── .gitignore
```

## Prerequisites

Before starting the project, ensure that you have:

- Docker installed
- Docker Compose installed
- Ports 5000, 9090, and 3000 available on your machine

## Configuration

Create a `.env` file in the project root:

```env
POSTGRES_DB=mydb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret
```

These values are used by both the Flask application and the PostgreSQL container.

## Getting Started

Clone the repository and move into the project folder:

```bash
cd flask-docker-stack
```

Start the stack:

```bash
docker-compose up --build
```

If you are using the newer Docker CLI, this is also valid:

```bash
docker compose up --build
```

After startup, the following services will be available:

- Flask API: http://localhost:5000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## API

### Root endpoint

```http
GET /
```

Example response:

```json
{
  "message": "Dockerized Flask API Running!"
}
```

### Metrics endpoint

```http
GET /metrics
```

This exposes Prometheus-formatted metrics for scraping.

## Prometheus Configuration

The project includes a basic `prometheus.yml` file that scrapes the Flask app:

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'flask_app'
    static_configs:
      - targets: ['web:5000']
```

## Grafana Setup

1. Open http://localhost:3000
2. Log in with:
   - Username: `admin`
   - Password: `admin`
3. Navigate to Configuration → Data Sources
4. Add a Prometheus data source
5. Set the URL to:
   - `http://prometheus:9090`
6. Save and test the connection

## Dockerfile

The application image is built from the root project directory using the following Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

## Health Checks

The Compose setup includes health checks for:

- the Flask service via HTTP on port 5000
- PostgreSQL using `pg_isready`
- Redis using `redis-cli ping`

## Troubleshooting

### Missing app path during build

If Docker reports that `app/requirements.txt` or `app/` is missing, make sure the Dockerfile is copying files from the project root instead of a nested directory.

### Services fail to start

Make sure your `.env` file exists and contains:

```env
POSTGRES_DB=mydb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret
```

### Grafana shows no data

Ensure Prometheus is running and that the Grafana Prometheus data source points to:

```text
http://prometheus:9090
```

## License

This project is intended for learning and local development use.

## Notes

This repository is intentionally simple and meant to illustrate how to run a Flask application with a monitoring stack in Docker Compose. It can serve as a foundation for building more advanced internal services or API backends.
