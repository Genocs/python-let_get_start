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

- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)
- [Conda](https://docs.conda.io/en/latest/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [FastAPI](https://fastapi.tiangolo.com/)


**Python** is a programming language that is actively developed and has a large community. It is used for web development (server-side), software development, mathematics, system scripting, data analysis, artificial intelligence, and scientific computing.

**Poetry** is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

**Conda** is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs, and updates packages and their dependencies.

**Docker** is a platform that enables developers to build, package, ship, and run applications in containers. Containers allow a developer to package up an application with all parts it needs, such as libraries and other dependencies, and ship it all out as one package.

**Docker Compose** is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.

**FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is designed to be easy to use and learn, and it is built on top of Starlette for the web parts and Pydantic for the data parts.

## 📚 Course Structure

The course is divided into chapters, and each chapter covers a specific topic. The chapters are as follows:
- [Chapter 1: Python Basics](./01-python-basics)
- [Chapter 2: Python Functions](./02-python-functions)
- [Chapter 3: Python Data Structures](./03-python-data-structures)
- [Chapter 4: Python Classes](./04-python-classes)
- [Chapter 5: Python Modules](./05-python-modules)
- [Chapter 6: Python Packages](./06-python-packages)
- [Chapter 7: Python Testing](./07-python-testing)
- [Chapter 8: Python Web Server](./08-python-web-server)
- [Chapter 9: Python Machine Learning](./09-python-machine-learning)
- [Chapter 10: Python Data Science](./10-python-data-science)



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
#docker build
docker build -t python-course ./10-web-uvicorn/.

# Run the docker container
docker run -d -p 8000:8000 python-course

```


```bash
```
docker-compose up
```
