from flask import Flask, jsonify, Response
import os
import psycopg2
import redis
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus counter for HTTP requests
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP Requests')

# PostgreSQL connection
db = psycopg2.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("POSTGRES_DB"),
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD")
)

# Redis connection
cache = redis.Redis(
    host=os.environ.get("REDIS_HOST"),
    port=6379
)

# Increment request counter before each request
@app.before_request
def before_request():
    REQUEST_COUNT.inc()

@app.route("/")
def home():
    return jsonify({"message": "Dockerized Flask API Running!"})

# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
