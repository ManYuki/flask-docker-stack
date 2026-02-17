Flask Production-Ready API 🚀

A containerized Flask backend with PostgreSQL, Redis caching, Prometheus monitoring, and Grafana dashboards.

🧱 Tech Stack

Flask

Docker & Docker Compose

PostgreSQL

Redis

Prometheus

Grafana

git

2️⃣ Run Containers
docker compose up -d

🔗 Services
Service	URL
Flask API	http://localhost:5000

Prometheus	http://localhost:9090

Grafana	http://localhost:3000
📊 Monitoring

Prometheus scrapes metrics from:

/metrics


Grafana dashboards visualize:

Total API requests

Request rate

Service health

❤️ Health Checks

Each container includes health checks to ensure reliability.

📌 Key Features

Dockerized microservice architecture

Caching with Redis

Persistent database with PostgreSQL

Production-style monitoring

Real-time dashboards