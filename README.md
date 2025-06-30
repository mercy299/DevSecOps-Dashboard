
# Security-Monitored Microservice Stack

## 🔧 Stack Components
- FastAPI microservice
- Prometheus for metrics
- Grafana for dashboards
- Falco for runtime security


## 📦  Project Structure Overview

```bash
devsecops-dashboard/
├── docker-compose.yml            # Main orchestration file
├── fastapi-app/                  # Simple FastAPI microservice
│   ├── main.py                   # API with a fast and slow endpoint
│   ├── requirements.txt
│   └── Dockerfile
├── prometheus/
│   └── prometheus.yml            # Scrapes metrics from FastAPI
├── diagram.png                   # Visual of architecture
└── README.md
```

## 🚀 Run the Stack
```bash
docker-compose up --build
```

## 📊 Access Services
- FastAPI: http://localhost:8000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (user: admin, pass: admin)

## ⚠️ Simulate Alert
```bash
docker exec -it <container_id_for_app> sh
curl http://example.com
```

## 📎 Falco Logs
```bash
docker logs <falco_container>
```

Run the command to confirm/check container Id or Name
```
docker ps
```
