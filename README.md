# 🖥️ Linux Server Monitoring Dashboard

A lightweight Linux server monitoring dashboard built with **Python, Flask, JavaScript, Docker, and Docker Compose**.

The project runs on a **Linux server hosted on AWS EC2** and collects real-time system information such as CPU, memory, disk usage, uptime, processes, IP address, and SSH status.

## ✨ Features

* Real-time CPU, memory, and disk monitoring
* Server health status: `Healthy`, `Warning`, `Critical`
* System uptime and running processes
* Server IP address and SSH status
* Interactive web dashboard
* Dockerized application using Docker Compose

## 🛠️ Tech Stack

* **Linux / AWS EC2**
* **Python & Flask**
* **HTML, CSS & JavaScript**
* **Docker & Docker Compose**

## 📂 Project Structure

```text
linux-monitoring-dashboard/
├── agent/
│   └── monitor.py
├── backend/
│   └── app.py
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚀 Run with Docker

> **Note:** The project must be run on a **Linux server**, such as an **AWS EC2 instance**.

On your Linux server, run:

```bash
git clone https://github.com/Youssef22s/linux-monitoring-dashboard.git
cd linux-monitoring-dashboard
docker compose up -d
```

After the containers start, open your **web browser** and visit:

```text
http://<EC2_PUBLIC_IP>:5000
```

Replace `<EC2_PUBLIC_IP>` with the public IP address of your EC2 instance.

For example:

```text
http://18.XXX.XXX.XXX:5000
```

Make sure **port 5000 is allowed in the EC2 Security Group**.

## 🎯 Project Goal

This project was built to practice and demonstrate practical knowledge of:

* Linux server administration
* AWS EC2
* Python & Flask
* REST APIs
* Docker & Docker Compose
* Linux system monitoring
* Basic DevOps concepts

