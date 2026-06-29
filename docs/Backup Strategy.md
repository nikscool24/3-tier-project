# Backup & Restart Strategy

This document explains how backups are handled for the Postgres database and how services are restarted to keep the system resilient.

---

## Backup Strategy (Postgres)

- Data is stored in a named Docker volume (`postgres-data`).
- To create a backup manually:
  ```bash
  docker exec postgres-container pg_dump -U $POSTGRES_USER $POSTGRES_DB > backup.sql

Always store backups off‑server (e.g., AWS S3, secure storage) to avoid losing data if the server fails.

## Restore Procedure
To restore from a backup:
docker exec -i postgres-container psql -U $POSTGRES_USER $POSTGRES_DB < backup.sql


## Automation
Backups can be automated using a cron job on the server.

Example: run a backup every day at 2 AM:

0 2 * * * docker exec postgres-container pg_dump -U $POSTGRES_USER $POSTGRES_DB > /backups/db-$(date +\%F).sql

This ensures daily backups are created automatically.

Rotate backups regularly (e.g., keep only the last 7–14 days) to avoid filling up storage.

## Restart Strategy
All critical services (Postgres, Redis, Backend, Frontend, Nginx) are configured with:

restart: always

This means containers will automatically restart if they crash or if the server reboots.

Ensures high availability without manual intervention.


## Summary
Restart → handled via Docker Compose (restart: always).

Backup → Postgres dumps scheduled via cron, stored off‑server.

Restore → simple psql command to reload data.

This setup ensures resilience, disaster recovery readiness, and smooth operation of the application stack.