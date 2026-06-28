Backup Strategy (Postgres)
Data stored in a named Docker volume (postgres-data).

Backup procedure:

bash
docker exec postgres-container pg_dump -U $POSTGRES_USER $POSTGRES_DB > backup.sql
Store backups off‑server (e.g., AWS S3, secure storage).

Restore procedure:

bash
docker exec -i postgres-container psql -U $POSTGRES_USER $POSTGRES_DB < backup.sql
Automation
Add cron job on server:

bash
0 2 * * * docker exec postgres-container pg_dump -U $POSTGRES_USER $POSTGRES_DB > /backups/db-$(date +\%F).sql
Ensures daily backups at 2 AM.

Rotate backups to avoid storage bloat.


Restart → handled via Docker Compose (restart: always).

Backup → Postgres dumps scheduled via cron, stored off‑server.

Restore → simple psql command to reload data.

Ensures resilience and disaster recovery readiness.