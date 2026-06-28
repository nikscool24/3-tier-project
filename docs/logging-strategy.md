# Logging Strategy

This project uses a **container‑based logging approach** where all services output logs to `stdout`/`stderr`.  
Docker captures these logs automatically, making them accessible via `docker logs`.

---

## Current Setup
- **Backend (FastAPI)** → Python logging configured to `stdout`.
- **Postgres, Redis, Nginx** → default logging to `stdout`.
- **Docker Compose** → aggregates logs from all containers.

---

## Viewing Logs
- Backend logs:
  ```bash
  docker logs <conatiner_id>
  docker compose logs -f backend

  docker compose logs -f reverseproxy

  docker compose logs -f postgres

#######################################################################
Rotation & Retention
Docker’s default json-file driver stores logs.

Configure log rotation in docker-compose.yml:

yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
Prevents disk exhaustion by limiting log size.