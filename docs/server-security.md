# Basic Server Security Measures

This project includes a baseline set of **server security practices** to ensure deployments are safe, reliable, and production‑ready.

---

## Access & Authentication
- Disable root login (`PermitRootLogin no` in `sshd_config`).
- Use SSH keys instead of passwords.
- Change default SSH port from `22` to a non‑standard port.
- Enable **fail2ban** to block brute‑force attempts.
- Create non‑root deployment users with limited `sudo` access.

---

##  Network & Firewall
- Use `ufw` or `iptables` to allow only required ports (22, 80, 443).
- Block all other ports by default.
- Redirect all HTTP traffic to HTTPS.
- Add security headers in Nginx (`Strict-Transport-Security`, `X-Frame-Options`, etc.).

---

##  Container Security
- Run containers as non‑root users.
- Use read‑only file systems for stateless services.
- Limit container capabilities (`cap_drop` in Docker Compose).
- Never bake secrets into images — inject via GitHub Secrets at runtime.

---

##  Monitoring & Logging
- Enable container healthchecks (backend, Postgres, Redis).
- Use centralized logging (ELK stack or Loki).
- Rotate logs to prevent disk exhaustion.
- Monitor system metrics with Prometheus + Grafana.

---

##  Updates & Maintenance
- Regularly update OS packages (`apt-get upgrade`).
- Keep Docker and Compose up to date.
- Rebuild images when base images release security patches.
- Backup Postgres volumes regularly and store off‑server (e.g., S3).

---

##  Extra Hardening
- Disable unused services (cron jobs, mail daemons, etc.).
- Apply resource limits (`ulimits`) to prevent runaway processes.
- Run audit tools (`lynis`, `clamav`) periodically.
- Automate TLS certificate renewal with Let’s Encrypt (production).
- **Password policy** → avoid special characters in DB password (to prevent connection string issues).

---

##  Summary
- Lock down SSH and firewall.  
- Run containers with least privilege.  
- Manage secrets securely via GitHub Secrets.  
- Monitor, patch, and back up regularly.  
- Use SSL/TLS (self‑signed for local, Let’s Encrypt for production).  

This ensures the deployment server is **secure, resilient, and production‑ready**.
