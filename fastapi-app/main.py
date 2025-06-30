from fastapi import FastAPI, Request
import time
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter("app_requests_total", "Total HTTP requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("app_request_latency_seconds", "Latency per endpoint", ["endpoint"])

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    resp_time = time.time() - start_time

    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(resp_time)

    return response

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/slow")
def slow_endpoint():
    time.sleep(2)
    return {"message": "Slow endpoint done."}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
