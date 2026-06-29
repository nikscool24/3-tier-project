# Simple Architecture Diagram

This project is built as a **3‑tier application** using Docker Compose.  
It shows how the frontend, backend, and database/cache work together behind an Nginx reverse proxy.

---

## Flow Explanation

1. **User (Browser)**  
   - When you open `http://localhost`, you land on the frontend UI.  
   - When you open `http://localhost/api`, you hit the backend service.

2. **Nginx Reverse Proxy**  
   - Acts as the single entry point.  
   - Routes `/` requests to the **Frontend (React)**.  
   - Routes `/api` requests to the **Backend (FastAPI)**.

3. **Frontend (React + Vite)**  
   - Shows a simple web page with an **Add User form** (Name + Number).  
   - When you click **Submit**, the data is sent to the backend API.  
   - On success, the page displays:  
     ```
     User saved successfully with ID <number>
     ```

4. **Backend (FastAPI)**  
   - Handles API requests.  
   - Visiting `/api` returns:  
     ```json
     {"message": "Hello World"}
     ```  
     which confirms the backend is running.  
   - Connects to **PostgreSQL** for persistent storage and **Redis** for caching.

5. **Database & Cache**  
   - **PostgreSQL** → stores user data (name, number, IDs).  
   - **Redis** → speeds up access by caching frequently used data.

6. **Docker Compose**  
   - Orchestrates all services (Frontend, Backend, Nginx, Postgres, Redis).  
   - Ensures everything runs together as one stack.

---

## Quick Summary
- **Frontend (`localhost`)** → UI form for adding users.  
- **Backend (`localhost/api`)** → API health check (`Hello World`).  
- **Nginx** → Routes traffic to the right service.  
- **Postgres + Redis** → Handle persistence and caching.  
- **Docker Compose** → Manages the entire stack.

This setup demonstrates a clean **3‑tier application** with reverse proxy and container orchestration.
