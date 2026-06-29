# Installing Docker & Docker Compose on Ubuntu

Before running this project, you’ll need Docker and Docker Compose installed on your system.  
Here’s a simple step‑by‑step guide I use on Ubuntu.

---

## Step 1: Update your system
Always start by updating packages:
```bash
sudo apt update
sudo apt upgrade -y

## Step 2: Install dependencies
Docker needs a few extra packages:

bash
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

## Step 3: Add Docker’s official GPG key
bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

## Step 4: Add Docker repository
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"


## Step 5: Install Docker
bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

## Check version:

bash
docker --version

## Run a quick test:

bash
sudo docker run hello-world

## Step 6: Run Docker without sudo
Add your user to the Docker group:

bash
sudo usermod -aG docker $USER

Log out and back in for this to take effect.

## Step 7: Install Docker Compose
Download the binary:

bash
sudo curl -L "https://github.com/docker/compose/releases/download/2.27.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


Make it executable:

bash
sudo chmod +x /usr/local/bin/docker-compose

Check version:

bash
docker-compose --version

At this point, Docker and Docker Compose are installed and ready.
You can now run the project with:

bash
docker-compose up or docker compose up