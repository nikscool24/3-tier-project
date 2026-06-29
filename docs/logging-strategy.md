# Logging Strategy

This project uses a **container‑based logging approach** where all services write logs to `stdout` and `stderr`.  
Docker automatically captures these logs, which makes them easy to view with `docker logs` or `docker compose logs`.

---

## Current Setup
- **Backend (FastAPI)** → Python logging configured to output to `stdout`.  
- **Postgres, Redis, Nginx** → default logging to `stdout`.  
- **Docker Compose** → aggregates logs from all containers so you can view them together.

---

## Viewing Logs
- Backend logs:
  ```bash
  docker logs <container_id>
  docker compose logs -f backend

## Nginx logs:
docker compose logs -f reverseproxy


## Postgres logs:
docker compose logs -f postgres

## Rotation & Retention
By default, Docker uses the json-file logging driver.
To prevent logs from growing too large and filling up disk space, configure log rotation in docker-compose.yml:

logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"

max-size: "10m" → each log file is capped at 10 MB.

max-file: "3" → keeps up to 3 rotated log files.

This setup prevents disk exhaustion while still keeping recent logs available

## Summary
All services log to stdout/stderr.

Logs can be viewed with docker logs or docker compose logs.

Rotation is configured to avoid disk issues.

Future improvements could include centralized logging (ELK, Loki, or CloudWatch).