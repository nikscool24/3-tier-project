# Docker Compose Setup

This project uses Docker Compose to run a complete application stack.  
The configuration defines five services — PostgreSQL, Redis, Backend, Frontend, and Nginx Reverse Proxy — all connected on a shared network.

---

## Services Breakdown

### PostgreSQL
- **Purpose**: Main database for the app.  
- **Details**:
  - Container name and image are set via environment variables.
  - Data is stored in a persistent volume (`postgres-data`) so it survives restarts.
  - Healthcheck uses `pg_isready` to make sure the DB is ready before other services start.
  - Exposes a host port mapped to the container port for external connections.

### Redis
- **Purpose**: In‑memory cache and message broker.  
- **Details**:
  - Container name and image are set via environment variables.
  - Healthcheck uses `redis-cli ping`.
  - Exposes a host port mapped to the container port.
  - Connected to the same network so the backend can talk to it.

### Backend
- **Purpose**: Core application logic (API service).  
- **Details**:
  - Depends on PostgreSQL (only starts when DB is healthy).
  - Environment variables define `DATABASE_URL` and `REDIS_URL`.
  - Healthcheck endpoint (`/health`) confirms service availability.
  - Exposes a host port mapped to the container port.

### Frontend
- **Purpose**: User interface.  
- **Details**:
  - Depends on the backend (ensures API is running before UI starts).
  - Container name and image are set via environment variables.
  - Exposes a host port mapped to the container port.

### Nginx Reverse Proxy
- **Purpose**: Entry point for all traffic, handles routing.  
- **Details**:
  - Depends on both backend and frontend.
  - Healthcheck uses `curl` to confirm proxy availability.
  - Exposes a host port mapped to the container port (usually port 80).
  - Routes requests correctly to backend or frontend.

---

## Volumes
```yaml
volumes:
  postgres-data:


Provides persistent storage for PostgreSQL data.

Ensures database state is not lost when containers are recreated.

## Networks

networks:
  project-network:
    driver: bridge


All services share a custom bridge network (project-network).

Allows secure communication between containers without exposing internal ports externally.

## Summary
This Docker Compose setup:

Defines a 3‑tier architecture (database, backend, frontend) with caching and reverse proxy.

Uses healthchecks so services only start when dependencies are ready.

Provides persistent storage for PostgreSQL.

Connects all services on a shared network for smooth communication.

Makes the stack portable and reproducible across environments.