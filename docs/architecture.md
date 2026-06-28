# Simple Architecture Diagram

This project follows a **3‑tier architecture** with Docker Compose orchestration:

---

##  Flow Explanation
1. **User (Browser)**  
   - Accesses the app via `http://localhost` (Frontend UI).  
   - Accesses API via `http://localhost/api` (Backend service).

2. **Nginx Reverse Proxy**  
   - Acts as the single entry point.  
   - Routes `/` requests to **Frontend (React)**.  
   - Routes `/api` requests to **Backend (FastAPI)**.

3. **Frontend (React + Vite)**  
   - Displays the UI with an **Add User form** (Name + Number).  
   - On submit → sends data to backend API.  
   - Shows confirmation:  
     ```
     User saved successfully with ID <number>
     ```

4. **Backend (FastAPI)**  
   - Handles API requests.  
   - `/api` endpoint returns:  
     ```json
     {"message": "Hello World"}
     ```  
     confirming backend is running.  
   - Connects to **PostgreSQL** (persistent storage) and **Redis** (cache).

5. **Database & Cache**  
   - **PostgreSQL** → stores user data (name, number, IDs).  
   - **Redis** → provides fast caching for backend operations.

6. **Docker Compose**  
   - Orchestrates all services (Frontend, Backend, Nginx, Postgres, Redis).  
   - Ensures containers run together as one stack.


- **Frontend (`localhost`)** → UI form for adding users.  
- **Backend (`localhost/api`)** → API health check (`Hello World`).  
- **Nginx** → Routes traffic to correct service.  
- **Postgres + Redis** → Handle persistence and caching.  
- **Docker Compose** → Manages the entire stack.

This design demonstrates a clean **3‑tier application** with reverse proxy and container orchestration.
