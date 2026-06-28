# 📄 Documentation for ci.yaml

{% code lineNumbers="true" %}
````
# Continuous Integration Workflow (`ci.yaml`)

This workflow automates the build and push process for all services in the project.  
It runs on every push to the `main` branch and ensures that Docker images are always up to date in Docker Hub.

---

## Workflow Breakdown

### Workflow Name
```yaml
name: CI
````
{% endcode %}

* The workflow is named **CI** to clearly indicate its purpose: Continuous Integration.

#### Trigger

yaml

```
on:
  push:
    branches: [main]
```

* The workflow runs automatically whenever code is pushed to the `main` branch.
* This ensures production images are always built from the latest stable code.

#### Job: Build and Push

yaml

```
jobs:
  build-and-push:
    runs-on: ubuntu-latest
```

* Defines a job called **build-and-push**.
* Runs on GitHub’s `ubuntu-latest` runner environment.

#### Matrix Strategy

yaml

```
    strategy:
      matrix:
        env_folder: [backend, frontend, nginx-reverseproxy]
```

* Uses a **matrix build** to run the same steps for three different services:
  * `backend`
  * `frontend`
  * `nginx-reverseproxy`
* This allows parallel builds, saving time and ensuring consistency across services.

#### Steps

**1. Checkout Code**

yaml

```
      - name: Checkout Code
        uses: actions/checkout@v7
```

* Pulls the latest code from the repository into the runner environment.

**2. Docker Login**

yaml

```
      - name: Docker Setup [Login]
        uses: docker/login-action@v4
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
```

* Logs into Docker Hub using GitHub Secrets for secure authentication.
* Credentials are never exposed in plain text.

**3. Docker Build and Push**

yaml

```
      - name: Docker Build and Push
        uses: docker/build-push-action@v7
        with:
          context: ./${{ matrix.env_folder }}
          push: true
          tags: |
            ${{ secrets.DOCKERHUB_USERNAME }}/project-${{ matrix.env_folder }}:latest
            ${{ secrets.DOCKERHUB_USERNAME }}/project-${{ matrix.env_folder }}:${{ github.sha }}
            ${{ secrets.DOCKERHUB_USERNAME }}/project-${{ matrix.env_folder }}:${{ github.ref_name }}
```

* Builds Docker images for each service from its respective folder.
* Pushes the images to Docker Hub with three tags:
  * `latest` → always points to the newest build.
  * `commit SHA` → uniquely identifies the exact commit.
  * `branch name` → useful for testing feature branches.

#### Job: Deploy

yaml

```
  deploy:
    needs: build-and-push
    uses: ./.github/workflows/cd.yaml
    secrets: inherit
```

* Defines a **deploy** job that runs after `build-and-push` completes.
* Reuses the `cd.yaml` workflow for deployment.
* Inherits secrets so deployment can authenticate with Docker Hub and other services.

### ✅ Summary

This CI workflow ensures:

* Every push to `main` automatically builds and pushes fresh Docker images.
* Images are tagged for traceability (`latest`, commit SHA, branch).
* Deployment is triggered seamlessly after builds succeed.
* The process is secure, automated, and consistent across all services.
