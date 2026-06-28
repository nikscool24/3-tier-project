# SSL Setup (Using Domain with Let's Encrypt)

In production, SSL should be configured with a trusted Certificate Authority (CA).  
This project uses **Let's Encrypt** (free, automated SSL certificates) with **Certbot** to secure traffic via Nginx.

---

## Prerequisites
- A registered domain (e.g., `example.com`).
- DNS records pointing the domain to your server’s public IP.
- Nginx reverse proxy running in Docker (from `nginx-reverseproxy/`).
- Port `80` (HTTP) and `443` (HTTPS) open on the server.

---

## Steps to Enable SSL with Let's Encrypt

### 1. Install Certbot
On the server:
```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx -y
2. Configure Nginx for Domain
Update nginx.conf:

nginx
server {
    listen 80;
    server_name example.com www.example.com;

    location / {
        proxy_pass http://frontend:3000;
    }

    location /api {
        proxy_pass http://backend:8000;
    }
}


3. Obtain SSL Certificate
Run Certbot:

bash
sudo certbot --nginx -d example.com -d www.example.com
Certbot will:

Verify domain ownership via HTTP challenge.

Automatically configure Nginx with SSL.

Generate certificates in /etc/letsencrypt/live/example.com/.

4. Auto‑Renew Certificates
Let’s Encrypt certificates expire every 90 days.
Set up auto‑renewal:

bash
sudo crontab -e
Add:

bash
0 0 * * * certbot renew --quiet


Docker Integration
If using Docker Compose:
Mount certificates into the Nginx container:

yaml
reverseproxy:
  container_name: ${NGINX_CONTAINER_NAME}
  image: ${NGINX_IMAGE}
  ports:
    - "80:80"
    - "443:443"
  volumes:
    - /etc/letsencrypt:/etc/letsencrypt:ro
  networks:
    - project-network



Self‑signed SSL → for local testing (shows “Not Secure”).

Let’s Encrypt SSL → for production with a domain (trusted by browsers).

Certificates are free, auto‑renewed, and fully integrated with Nginx.

Users accessing https://example.com will see a secure green lock