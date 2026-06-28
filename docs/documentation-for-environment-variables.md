# 📄 Documentation for Environment Variables

```
# Environment Variables

This project uses a `.env` file to manage configuration for all services.  
The file is generated dynamically during deployment, pulling values from **GitHub Secrets** (sensitive data) and **GitHub Variables** (non-sensitive configs).

---

## Why Environment Variables?
- Keep sensitive data (like passwords) out of source code.  
- Allow flexible configuration across environments (dev, staging, production).  
- Make Docker Compose deployments portable and secure.

---

## Variables Breakdown

### PostgreSQL
- `POSTGRES_CONTAINER_NAME` → Name of the Postgres container.  
- `POSTGRES_IMAGE` → Docker image used for Postgres.  
- `POSTGRES_HOST_PORT` → Port exposed on the host machine.  
- `POSTGRES_CONTAINER_PORT` → Internal container port.  
- `POSTGRES_USER` → Database username (stored in GitHub Secrets).  
- `POSTGRES_PASSWORD` → Database password (stored in GitHub Secrets).  
- `POSTGRES_DB` → Database name.

### Redis
- `REDIS_CONTAINER_NAME` → Name of the Redis container.  
- `REDIS_IMAGE` → Docker image used for Redis.  
- `REDIS_HOST_PORT` → Port exposed on the host machine.  
- `REDIS_CONTAINER_PORT` → Internal container port.

### Backend
- `BACKEND_CONTAINER_NAME` → Name of the backend container.  
- `BACKEND_IMAGE` → Docker image for backend service.  
- `BACKEND_HOST_PORT` → Port exposed on host.  
- `BACKEND_CONTAINER_PORT` → Internal port inside container.

### Frontend
- `FRONTEND_CONTAINER_NAME` → Name of the frontend container.  
- `FRONTEND_IMAGE` → Docker image for frontend service.  
- `FRONTEND_HOST_PORT` → Port exposed on host.  
- `FRONTEND_CONTAINER_PORT` → Internal port inside container.

### Nginx Reverse Proxy
- `NGINX_CONTAINER_NAME` → Name of the Nginx container.  
- `NGINX_IMAGE` → Docker image for Nginx reverse proxy.  
- `NGINX_HOST_PORT` → Port exposed on host (usually 80/443).  
- `NGINX_CONTAINER_PORT` → Internal port inside container.

---

## Storage Locations
- **GitHub Secrets** → Used for sensitive values (passwords, usernames, private images).  
- **GitHub Variables** → Used for non-sensitive configs (container names, ports, image names).  
- **.env file** → Generated at runtime on the server, never committed to source control.

---

## ✅ Summary
By separating secrets and configs:
- The pipeline stays secure (no hardcoded passwords).  
- Deployment is consistent across environments.
```
