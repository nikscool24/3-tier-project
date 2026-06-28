## Documentation for docker-compose.yaml

````
# Docker Compose Setup

This project uses Docker Compose to orchestrate a complete application stack.  
The configuration defines five services — PostgreSQL, Redis, Backend, Frontend, and Nginx Reverse Proxy — all connected on a shared network.

---

## Services Breakdown

### PostgreSQL
- **Purpose**: Primary database for the application.  
- **Key Configurations**:
  - Container name and image defined via environment variables.
  - Persistent volume (`postgres-data`) ensures data survives container restarts.
  - Healthcheck using `pg_isready` to confirm database readiness.
  - Exposes host port mapped to container port for external connections.

### Redis
- **Purpose**: In‑memory cache and message broker.  
- **Key Configurations**:
  - Container name and image defined via environment variables.
  - Healthcheck using `redis-cli ping`.
  - Exposes host port mapped to container port.
  - Connected to the same project network for communication with backend.

### Backend
- **Purpose**: Core application logic (API service).  
- **Key Configurations**:
  - Depends on PostgreSQL (only starts when DB is healthy).
  - Environment variables define `DATABASE_URL` and `REDIS_URL`.
  - Healthcheck endpoint (`/health`) ensures service availability.
  - Exposes host port mapped to container port.

### Frontend
- **Purpose**: User interface layer.  
- **Key Configurations**:
  - Depends on backend (ensures API is running before UI starts).
  - Container name and image defined via environment variables.
  - Exposes host port mapped to container port.

### Nginx Reverse Proxy
- **Purpose**: Entry point for all traffic, load balancing and routing.  
- **Key Configurations**:
  - Depends on both backend and frontend.
  - Healthcheck using `curl` to confirm proxy availability.
  - Exposes host port mapped to container port (typically port 80).
  - Ensures requests are routed correctly to backend/frontend.

---

## Volumes
```yaml
volumes:
  postgres-data:
````

* Provides persistent storage for PostgreSQL data.
* Ensures database state is not lost when containers are recreated.

### Networks

yaml

```
networks:
  project-network:
    driver: bridge
```

* All services share a custom bridge network (`project-network`).
* Enables secure inter‑service communication without exposing internal ports externally.



This Docker Compose setup:

* Defines a **complete 3‑tier architecture** (database, backend, frontend) with caching and reverse proxy.
* Uses **healthchecks** to ensure services only start when dependencies are ready.
* Provides **persistent storage** for PostgreSQL.
* Connects all services on a **shared network** for seamless communication.
* Makes the stack portable and reproducible across environments.
