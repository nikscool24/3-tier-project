# Installing a GitHub Self‑Hosted Runner

This guide walks you through installing and registering a **self‑hosted GitHub Actions runner** on your server.  
The runner allows your CI/CD workflows to execute directly on your own machine instead of GitHub’s hosted runners.

---

## Step 1: Go to Your Repository Settings
1. Open your repository on GitHub.
2. Click on **Settings** (top menu bar).
3. Scroll down the left sidebar and click **Actions → Runners**.
4. Click the **New self‑hosted runner** button.

---

## Step 2: Choose Operating System
1. GitHub will ask you to select the OS for your runner.  
   - Choose **Linux** if you’re installing on Ubuntu.
2. It will show you a set of commands to run on your server.

---

## Step 3: Download the Runner Package
On your server, run the commands GitHub provides. Example:
```bash
# Create a folder for the runner
mkdir actions-runner && cd actions-runner

# Download the latest runner package
curl -o actions-runner-linux-x64-2.317.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.317.0/actions-runner-linux-x64-2.317.0.tar.gz

# Extract the package
tar xzf ./actions-runner-linux-x64-2.317.0.tar.gz


## Step 4: Configure the Runner
GitHub will give you a registration command. It looks like this:
./config.sh --url https://github.com/<your-username>/<your-repo> --token <registration-token>

Replace <your-username> and <your-repo> with your repository details.

Use the registration token provided in the GitHub UI when you clicked “New self‑hosted runner”.

Follow the prompts:

Enter a name for the runner (e.g., my-server-runner).

Choose a work folder (default is _work).

Select labels (optional, e.g., ubuntu, docker).


## Step 5: Start the Runner
Run: ./run.sh
This starts the runner process. You should see logs showing it’s listening for jobs.


## Step 6: Install as a Service (Recommended)
To keep the runner running after reboot:
sudo ./svc.sh install
sudo ./svc.sh start


## Step 7: Verify on GitHub
Go back to Settings → Actions → Runners in your repository.

You should now see your server listed as Online.

Try running a workflow — it should execute on your self‑hosted runner.

## Summary
Navigate to Settings → Actions → Runners → New self‑hosted runner.

Download and extract the runner package on your server.

Configure it with your repo URL and token.

Start the runner and optionally install it as a service.

Verify it shows up as Online in GitHub.

Once installed, your CI/CD pipelines will run directly on your server, giving you full control over the environment.