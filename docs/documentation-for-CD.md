# 📄 Documentation for cd.yaml

````
# Continuous Deployment Workflow (`cd.yaml`)

This workflow handles the deployment of Docker containers to the self‑hosted server.  
It is triggered automatically by the CI pipeline once images are built and pushed to Docker Hub.

---

## Workflow Breakdown

### Workflow Name
```yaml
name: CD
````

* Named **CD** to clearly indicate its purpose: Continuous Deployment.

#### Trigger

yaml

```
on:
  workflow_call:
```

* This workflow is not triggered directly by a branch push.
* Instead, it is **called by the CI workflow** (`ci.yaml`) after successful builds.
* This ensures deployment only happens when images are ready.

#### Job: Deploy

yaml

```
jobs:
  deploy:
    runs-on: self-hosted
```

* Defines a job called **deploy**.
* Runs on a **self‑hosted runner** (your own server), so containers are deployed directly where they need to run.

#### Steps

**1. Checkout Code**

yaml

```
      - name: Checkout Code
        uses: actions/checkout@v7
```

* Pulls the latest repository files into the server.
* Ensures deployment uses the newest codebase.

**2. Docker Login**

yaml

```
      - name: Docker Setup [Login]
        uses: docker/login-action@v4
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
```

* Authenticates with Docker Hub using GitHub Secrets.
* Allows the runner to pull private images securely.

**3. Write `.env` File**

yaml

```
      - name: Write .env file
        run: |
          cat <<EOF > .env
          POSTGRES_CONTAINER_NAME=${{ vars.POSTGRES_CONTAINER_NAME }}
          POSTGRES_IMAGE=${{ vars.POSTGRES_IMAGE }}
          POSTGRES_HOST_PORT=${{ secrets.POSTGRES_HOST_PORT }}
          POSTGRES_CONTAINER_PORT=${{ vars.POSTGRES_CONTAINER_PORT }}
          POSTGRES_USER=${{ secrets.POSTGRES_USER }}
          POSTGRES_PASSWORD=${{ secrets.POSTGRES_PASSWORD }}
          POSTGRES_DB=${{ secrets.POSTGRES_DB }}
          ...
          EOF
```

* Dynamically generates a fresh `.env` file on every run.
* Pulls values from **GitHub Secrets** (sensitive data like passwords) and **GitHub Variables** (non‑sensitive configs like container names).
* This ensures environment variables are always up to date and secure.

**4. Run Deployment with Docker Compose**

yaml

```
      - name: Run the Deployment of containers with Docker Compose
        run: |
          docker compose --env-file .env pull
          docker compose --env-file .env up -d --force-recreate --pull always
```

* Uses Docker Compose to:
  * **Pull** the latest images from Docker Hub.
  * **Recreate containers** with updated images and environment variables.
  * Run them in detached mode (`-d`) so services stay live.
* The `--force-recreate` flag ensures old containers are replaced cleanly.
* The `--pull always` flag guarantees the newest image version is used.

### ✅ Summary

This CD workflow ensures:

* Deployment only happens after CI builds succeed.
* Environment variables are securely injected from GitHub Secrets/Variables.
* Containers are recreated with the latest images every run.
* The process is automated, consistent, and secure — no manual intervention needed.
