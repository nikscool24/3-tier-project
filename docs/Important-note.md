# Important Note: Manual Installation Required

Before running this project in a real environment, there are a few things that **must be installed manually on the server**:

- **Docker**
- **Docker Compose**
- **GitHub Self‑Hosted Runner**

---

## Why Manual Installation?

1. **Docker & Docker Compose**
   - These tools are the backbone of the project.  
   - Docker runs each service (frontend, backend, database, cache, reverse proxy) in isolated containers.  
   - Docker Compose ties them together into one stack.  
   - Installing them manually ensures you’re using the correct version for your server and avoids issues with automated scripts that may fail on different Linux distributions.

2. **Self‑Hosted Runner**
   - The CI/CD pipeline relies on a GitHub Actions runner that lives on your server.  
   - This runner executes workflows (build, scan, push, deploy).  
   - It must be installed manually because it needs to be registered with your GitHub repository and linked to your server’s environment.  
   - Manual setup guarantees that secrets, permissions, and environment variables are configured securely.

---

## Recommended Approach

- **Step 1:** Install Docker and Docker Compose following the [install-docker.md](./install-docker.md) guide.  
- **Step 2:** Install the GitHub self‑hosted runner by downloading it from GitHub and registering it with your repo.  
- **Step 3:** Verify that both Docker and the runner are working before running any CI/CD pipelines.  
- **Step 4:** Keep these tools updated manually to avoid compatibility issues.

---

## Summary

- Docker and Docker Compose are required to run the application stack.  
- The self‑hosted runner is required to execute CI/CD workflows on your server.  
- All three must be installed manually to ensure stability, security, and proper integration with your environment.  
- Once installed, the project can be deployed smoothly using `docker-compose up` and GitHub Actions.
