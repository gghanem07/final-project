Final Project
Project Overview

This project is a full-stack calculator management application built using FastAPI, PostgreSQL, Docker, and JWT authentication. Users can securely register, log in, create calculations, edit calculations, delete calculations, and manage their calculation history through a modern web interface.

The application follows BREAD operations (Browse, Read, Edit, Add, Delete) and includes an advanced Undo/Redo feature for calculation updates.

# Features 

## Authentication & Security
User registration and login
JWT-based authentication
Password hashing for secure credential storage
Protected API routes
User-specific calculation access

## Calculation Features
Addition
Subtraction
Multiplication
Division

## BREAD Operations
Browse all calculations
Read/view individual calculations
Add new calculations
Edit existing calculations
Delete calculations

## Advanced Feature: Undo / Redo
Undo previous calculation updates
Redo reverted calculation updates
Dynamic UI button enabling/disabling
State tracking for calculation history

## Front-End Features
Responsive dashboard UI
View and edit calculation pages
Real-time user feedback messages
Undo/Redo button state management

## Technologies Used
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
Docker
Docker Compose
JWT Authentication
Playwright
Pytest
GitHub Actions
HTML / Tailwind CSS / JavaScript

## Project Structure
app/
├── models/
├── routes/
├── schemas/
├── templates/
├── auth/
├── services/
└── main.py

tests/
├── unit/
├── integration/
└── e2e/

## Running the Application
Clone the Repository
git clone https://github.com/gghanem07/final-project.git
cd final-project

## Build and Start Containers
docker compose up --build

## Access the Application

Application:

http://localhost:8000

Swagger API Docs:

http://localhost:8000/docs

pgAdmin:

http://localhost:5050

# Running Tests

## Run Full Test Suite
docker compose exec web pytest --no-cov
## Run Specific Test Suites
Integration Tests
docker compose exec web pytest tests/integration --no-cov
E2E Tests
docker compose exec web pytest tests/e2e --no-cov
Unit Tests
docker compose exec web pytest tests/unit --no-cov

## CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration and Continuous Deployment.

The pipeline automatically:

Runs all tests
Builds the Docker image
Pushes the image to Docker Hub after successful builds

## Docker Hub Repository

Docker Image Repository:

https://hub.docker.com/repository/docker/gghanem07/assignment14/general

GitHub Repository

Repository Link:

https://github.com/gghanem07/final-project

## Testing Coverage

The project includes:

Unit Tests
Integration Tests
End-to-End (E2E) Tests

Testing validates:

Authentication workflows
Calculation logic
API endpoints
Undo/Redo functionality
Front-end workflows

## Security Features
JWT authentication
Password hashing
User authorization checks
Input validation with Pydantic
Protected calculation ownership