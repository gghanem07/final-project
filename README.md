# Assignment 14 – FastAPI Calculator (BREAD Operations)

## Overview
This project is a full-stack FastAPI application that allows users to perform and manage calculations. It implements BREAD (Browse, Read, Edit, Add, Delete) functionality with authentication, database integration, testing, and CI/CD.

## Features
- User registration and login (JWT authentication)
- Add new calculations
- Browse all user calculations
- Read/view specific calculations
- Edit existing calculations
- Delete calculations
- Fully tested with unit, integration, and end-to-end tests

---

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose
- Pytest (unit, integration, e2e)
- GitHub Actions (CI/CD)

---

## How to Run the Application

```bash
docker compose up --build

to open the site: 
   http://localhost:8000

How to Run Tests:
   docker compose exec web pytest --no-cov

Docker Hub:
Docker image is available at
   https://hub.docker.com/r/gghanem07/assignment14

CI/CD:
GitHub Actions is configured to:
   Run tests automatically
   Build Docker image
   Scan for vulnerabilities
   Push image to Docker Hub

BREAD Functionality:
   Browse: View all user calculations
   Read: View details of a specific calculation
   Edit: Update calculation values
   Add: Create new calculations
   Delete: Remove calculations

