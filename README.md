# DSO101 Assignment IV

## Project Title
Deploy Your First Web App using GitHub and Render

## Project Overview
This project is a simple Flask web application created for DSO101 Assignment IV. The aim of this assignment is to learn the basics of Git, GitHub, GitHub Actions, and Render deployment.

The application displays a simple webpage showing that the project has been created and deployed successfully.

## Tools and Technologies Used
- Python
- Flask
- Gunicorn
- Git
- GitHub
- GitHub Actions
- Render

## Project Files
- app.py: Main Flask application file
- requirements.txt: Python dependencies
- README.md: Project documentation
- .github/workflows/deploy.yml: GitHub Actions workflow file

## How the Application Works
The application uses Flask to create a simple web server. When the user opens the homepage, the app displays a message for DSO101 Assignment IV.

## GitHub Actions Workflow
A GitHub Actions workflow was added to the project. The workflow runs automatically whenever code is pushed to the main branch.

The workflow performs these steps:
1. Checks out the repository code
2. Runs a dummy step to confirm that the code was pushed successfully

## Render Deployment
The project was deployed using Render as a web service.

Render settings used:

Build Command:
```bash
pip install -r requirements.txt
