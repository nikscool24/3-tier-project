## Project-structure.md

````
# Project Structure & Summary

This project is a **3‑tier application** built with Docker Compose, integrating:
- **Frontend (React)** → User interface
- **Backend (FastAPI)** → API service
- **Database (PostgreSQL)** → Persistent storage
- **Cache (Redis)** → In‑memory caching
- **Reverse Proxy (Nginx)** → Entry point and traffic routing

---

## 📂 File Structure

.
├── backend/              # FastAPI backend service (main.py, Dockerfile)
├── frontend/             # React frontend (UI, Dockerfile)
├── init/postgres/        # Database schema + seed data
├── nginx-reverseproxy/   # Nginx reverse proxy configuration + Dockerfile
├── docker-compose.yml    # Orchestration of all services
├── Makefile              # Shortcuts for common commands
├── .github/workflows/    # CI/CD pipelines (ci.yaml, cd.yaml)
├── .env.example          # Reference environment variables (Secrets vs Variables)
└── README.md             # Project documentation

Code

---

## Request Flow

### 1. User hits `http://localhost`
- Request goes to **Nginx reverse proxy**.  
- Nginx forwards traffic to the **Frontend container**.  
- The frontend displays a simple webpage with a form:
  - **Add User** → fields for `name` and `number`.  
  - **Submit button** → sends data to the backend API.  
- On successful submission, the page shows:  
 User saved successfully with ID <number>


### 2. User hits `http://localhost/api`
- Request goes to **Nginx reverse proxy**.  
- Nginx forwards traffic to the **Backend container** (FastAPI).  
- Backend responds with:
```json
{"message": "Hello World"}
This confirms the backend server is running and reachable.

Summary
Frontend (localhost) → Displays a form to add user data (name + number).

Backend (localhost/api) → Returns a simple JSON response (Hello World) to confirm API health.

Nginx Reverse Proxy → Routes requests to the correct service (Frontend or Backend).

Postgres + Redis → Support data persistence and caching for backend operations.

Docker Compose → Orchestrates all services into one stack.

This design demonstrates a complete 3‑tier architecture with clear separation of concerns:

UI Layer → React frontend

Logic Layer → FastAPI backend

Data Layer → PostgreSQL + Redis

Entry Point → Nginx reverse proxy
````
Rest all other details related to this project are located in docs folder on root location of this project.