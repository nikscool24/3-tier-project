# Security Scanning in CI Pipeline

This project integrates **security scanning** directly into the CI workflow to ensure Docker images are safe before deployment.

---

## Why Security Scanning?
- Detect vulnerabilities in base images and dependencies.
- Enforce best practices in Dockerfiles.
- Prevent insecure images from being pushed to DockerHub.
- Maintain production-grade security standards.

---

## Workflow Breakdown

### 1. Dockerfile Lint (Hadolint)
- Each service (`backend`, `frontend`, `nginx-reverseproxy`) runs through **Hadolint**.
- Hadolint checks for:
  - Best practices (e.g., using `COPY` instead of `ADD`).
  - Avoiding root user in containers.
  - Proper use of pinned versions.
- Ensures Dockerfiles are clean, consistent, and secure.

### 2. Docker Build (with `--no-cache`)
- Builds a Docker image for each service with:
  ```bash
  docker build -t <username>/project-<service>:latest --no-cache


##### Vulnerability Scan (Trivy)
Runs Trivy against each built image.

Configuration:

vuln-type: os,library → scans both OS packages and application libraries.

severity: CRITICAL → fails the pipeline if critical vulnerabilities are found.

ignore-unfixed: true → ignores vulnerabilities without available fixes.

continue-on-error: true → logs results but allows pipeline to continue for visibility.

Output format: table for easy readability in GitHub Actions logs.

✅ Summary
Hadolint → enforces Dockerfile best practices.

Docker Build with --no-cache → ensures fresh images are scanned.

Trivy → scans images for vulnerabilities before pushing.

Build-and-Push → only runs if lint/scan jobs succeed.

Deploy → inherits secrets and runs CD workflow with secure images.

This ensures every image deployed is linted, scanned, and verified before reaching production.