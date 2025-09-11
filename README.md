# 📌loto-server
`loto-server` contains the Docker configurations for hosting and running the PDF report generation service


![GitHub License](https://img.shields.io/github/license/kmschang/loto-server)
![GitHub Release](https://img.shields.io/github/v/release/kmschang/loto-server)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/kmschang/loto-server)
![GitHub last commit](https://img.shields.io/github/last-commit/kmschang/loto-server)

---

## 📦 Contents

- [`Dockerfile`](Dockerfile) — Defines the container for the PDF report generator (sets up the environment, dependencies, entrypoint, etc.).

- [`docker-compose.yml`](docker-compose.yml) — Orchestrates service startup, linking necessary services (if any), managing volumes or ports, and making it easy to launch locally or in production.

- [`app/`](app)— (Assuming this is where the report generation code lives) The application logic that generates the PDFs.

---

## 🚀 Usage

1. Clone this repository:
```bash
git clone git@github.com:kscardinal/custom-rsa-keys.git
cd loto-server
```

2. Build the Docker image:
```bash
docker build -t loto-server .
```

3. Or use Docker Compose to build and run everything:
```bash
docker-compose up -d
```
- The service will then be available (on whatever port you've configured via `docker-compose.yml`) and will generate PDF reports based on incoming requests / jobs.

---

## ⚙️ Configuration

- You may need to adjust environment variables in `docker-compose.yml` (e.g. for paths, credentials, or external services).
- Exposed ports, volume mounts, and resource limits are controlled via the compose file so you can tailor them to your deployment environment.
- The `Dockerfile` installs dependencies, copies the app code, sets up any required system libs, and defines the default command to start the PDF generation service.

---

## 🛠️ Development & Deployment Tips

- To test locally, use `docker-compose` so that logs, ports, and file mounts are managed.
- For updates, rebuild the image (or use `docker-compose build`) and restart.
- Use CI/CD to automate building, testing, and pushing Docker images, then deploying them to your server or container host.

---

## 📜 Version

This is version **1.0.0** as of _Sep 11, 2025._

---

## 🔑 License

This project is licensed under the MIT License, which means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, as long as you include the original copyright and license notice in any copy of the software. The software is provided "as is," without warranty of any kind.
