# 📖 Python Course

## Overview

This project is a Python course that teaches users how to start coding in Python.
The course is designed to help users learn Python from scratch, and it covers the following topics:

- Poetry integration for python dependency handler
- Python Web Server with FastAPI and Uvicorn
- Python Machine Learning
  - Langchain
  - Scikit-learn
- Python Data Science

## Getting Started

Before you begin, ensure you have the following software installed and provisioned:

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)

**Docker** is a platform that enables developers to build, package, ship, and run applications in containers. Containers allow a developer to package up an application with all parts it needs, such as libraries and other dependencies, and ship it all out as one package.

**Python** is a programming language that is actively developed and has a large community. It is used for web development (server-side), software development, mathematics, system scripting, data analysis, artificial intelligence, and scientific computing.

**Poetry** is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

## Setup

To initialize the project, you'll need to create a `.env` file at the root of the project. This file should contain all of the environment variables required by the project. Use the `.env.example` file as a template.

## 💻 Running Locally

1. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment🔨

2. If you don't have poetry installed, you can install it with `pip install poetry`.
3. Add `poetry` to your path.
4. Move to the project directory and run the following commands:

   ```bash
   # To check if poetry is installed [Tested with 1.6.1]
   poetry --version

   # To reevaluate the dependencies
   poetry lock

   # To install the dependencies
   poetry install --no-root

   # Setup the environment variables
   mv ./src/env.example ./src/.env

   # To activate the virtual environment
   poetry shell
   ```

5. Select the chapter

   ```bash
   cd ./10-web-uvicorn
   # Setup libraries *(not mandatory)
   pip install -r ./requirements.txt

   # Run the FastAPI server
   cd ./10-web-uvicorn/src
   uvicorn app.main:app --reload
   ```

6. Display the API documentation

   - Open the following links in your browser to view the API documentation by using ReDoc
   
     - [ReDoc](http://127.0.0.1:8000)

   - Open the following links in your browser to view the API documentation by using the Swagger UI

     - [Swagger UI](http://127.0.0.1:8000/docs)

## 💻 Running with Docker

To run the project with docker, execute the following command:

```bash
docker-compose up
```
