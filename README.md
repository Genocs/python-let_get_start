# 📖 Python Course

## Overview

This project is a Python course that teaches users how to start coding in Python.
The course is designed to help users learn Python from scratch, and it covers the following topics:

- **python**
  - basics (variables, data types, operators, etc.)
  - functions (functions, lambda functions, etc.)
  - data structures (lists, tuples, dictionaries, sets, etc.)
  - classes (classes, objects, inheritance, etc.)
- **Poetry** integration for python dependency handler
- **Conda** integration for python environment management
- python Web Server with **FastAPI** and **Uvicorn**
- python DS (Data Science):
  - **Pandas**
  - **Numpy**
  - **Matplotlib**
  - **Seaborn**
  - **Jupyter**
  - **Scikit-learn**
- python LLM (Large Language Model):
  - **Promptflow**
  - **Langchain**
  - **Autogen**

## Getting Started

Before you begin, ensure you have the following software installed and provisioned:

- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)
- [Conda](https://docs.conda.io/en/latest/)
- [Docker](https://www.docker.com/)


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
- [Chapter 8: Python Web Server with FastAPI and Uvicorn](./08-python-web-server)
- [Chapter 9: Python Machine Learning](./09-python-machine-learning)
- [Chapter 10: Python Data Science](./10-python-data-science)
- [Chapter 11: Python Langchain](./11-python-langchain/README.md)
- [Chapter 12: Python Promptflow](./12-python-promptflow)
- [Chapter 13: Python Autogen](./13-python-autogen)

## List of libraries used in the project

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Jupyter](https://jupyter.org/)
- [Promptflow](https://microsoft.github.io/promptflow/)
- [Langchain](https://langchain.com/)
- [Autogen](https://microsoft.github.io/autogen/)

## Setup

To initialize the project, you'll need to create a `.env` file at the root of each folder. 

This file should contain all of the environment variables required by the project. Use the `.env.example` file as a template.

The dependencies for the project are managed using Poetry.


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
docker build -t web-uvicorn ./10-web-uvicorn/.

# Run the docker container with container name and port mapping
docker run -d --name web-uvicorn_01 -p 8200:8000 web-uvicorn
```

```bash
docker-compose up
```

## 📝 Testing

To run the tests, execute the following command:

```bash
# Run the tests
pytest
```

## 🚀 Deployment

To deploy the project, you'll need to follow the steps below:

1. Install Docker and Docker Compose on your server.
2. Clone the project repository on your server.
3. Create a `.env` file at the root of the project and add the required environment variables.
4. Run the following command to start the project:

```bash
docker-compose up
```

## 🛡️ Security

If you discover any security-related issues, please email

## 🤝 Contributing



## Cap. 1: Python Basics

### 1.1 Variables

- Variables are used to store data values in memory.
- Variables are created when you assign a value to them.
- Variables can store different types of data, such as numbers, strings, lists, etc.

### 1.2 Data Types

- Python has several built-in data types, such as int, float, str, list, tuple, dict, set, etc.
- Each data type has its own set of operations and methods.

### 1.3 Operators

- Operators are used to perform operations on variables and values.
- Python has several types of operators, such as arithmetic, comparison, logical, bitwise, etc.

### 1.4 Control Structures

- Control structures are used to control the flow of a program.
- Python has several control structures, such as if-else, for loop, while loop, etc.

### 1.5 Functions

- Functions are used to group code into reusable blocks.
- Functions can take parameters and return values.

### 1.6 Modules

- Modules are used to organize code into separate files.
- Modules can be imported into other modules to use their functionality.

### 1.7 Packages

- Packages are used to organize modules into separate directories.
- Packages can contain sub-packages and modules.

### 1.8 Testing

- Testing is used to verify that the code works as expected.
- Python has several testing frameworks, such as unittest, pytest, etc.

## Cap. 2: Python Functions

### 2.1 Functions

- Functions are used to group code into reusable blocks.
- Functions can take parameters and return values.

### 2.2 Lambda Functions

- Lambda functions are used to create small anonymous functions.
- Lambda functions can take any number of arguments, but they can only have one expression.

### 2.3 Decorators

- Decorators are used to modify the behavior of functions or methods.
- Decorators are a powerful tool in Python, and they are used in many libraries and frameworks.

### 2.4 Generators

- Generators are used to create iterators in Python.
- Generators are a powerful tool for working with large datasets.

### 2.5 Closures

- Closures are used to create nested functions in Python.
- Closures are a powerful tool for creating modular and reusable code.

## Cap. 3: Python Data Structures

### 3.1 Lists

- Lists are used to store multiple items in a single variable.
- Lists are mutable, which means you can change the items in a list.

### 3.2 Tuples

- Tuples are used to store multiple items in a single variable.
- Tuples are immutable, which means you cannot change the items in a tuple.

### 3.3 Dictionaries

- Dictionaries are used to store key-value pairs in Python.
- Dictionaries are mutable, which means you can change the items in a dictionary.

### 3.4 Sets

- Sets are used to store unique items in Python.

## Cap. 4: Python Classes

### 4.1 Classes

- Classes are used to create objects in Python.
- Classes are a powerful tool for creating modular and reusable code.

### 4.2 Objects

- Objects are instances of classes in Python.
- Objects have attributes and methods that define their behavior.

### 4.3 Inheritance

- Inheritance is used to create new classes that inherit the properties and methods of existing classes.
- Inheritance is a powerful tool for creating modular and reusable code.

### 4.4 Polymorphism

- Polymorphism is the ability of an object to take on many forms.
- Polymorphism is a powerful tool for creating modular and reusable code.

## Cap. 5: Python Modules

### 5.1 Modules

- Modules are used to organize code into separate files.
- Modules can be imported into other modules to use their functionality.

### 5.2 Packages

- Packages are used to organize modules into separate directories.


## Cap. 6: Python Packages

### 6.1 Packages

- Packages are used to organize modules into separate directories.
- Packages can contain sub-packages and modules.

## Cap. 7: Python Testing

### 7.1 Testing

- Testing is used to verify that the code works as expected.
- Python has several testing frameworks, such as unittest, pytest, etc.

## Cap. 8: Python Web Server with FastAPI and Uvicorn

### 8.1 FastAPI

- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

### 8.2 Uvicorn

- Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

## Cap. 9: Python Machine Learning


## Cap. 10: Python Data Science

### 10.1 Pandas

- Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and data manipulation library built on top of the Python programming language.

### 10.2 Numpy

- Numpy is a powerful library for numerical computing in Python.

### 10.3 Matplotlib

- Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

### 10.4 Seaborn

- Seaborn is a Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.

### 10.5 Jupyter

- Jupyter is a free, open-source, interactive web tool known as a computational notebook, which researchers can use to combine software code, computational output, explanatory text, and multimedia resources in a single document.

### 10.6 Scikit-learn

- Scikit-learn is a free software machine learning library for the Python programming language. It features various classification, regression, and clustering algorithms, including support vector machines, random forests, gradient boosting, k-means, and DBSCAN.

## Cap. 11: Promptflow

## Cap. 11.1: Promptflow

- Promptflow is a large language model that generates text based on a given prompt.


## Cap. 12: Python Langchain

### 12.1 Langchain

- Langchain is a large language model that generates text based on a given prompt.


## Cap. 13: Python Promptflow

### 13.1 Promptflow

- Promptflow is a large language model that generates text based on a given prompt.


## Cap. 14: Python Autogen

### 14.1 Autogen

- Autogen is a large language model that generates text based on a given prompt.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📧 Contact

If you have any questions, please feel free to reach out to me at [email](mailto:)

## 🚀 Resources

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/)
- [Conda](https://docs.conda.io/en/latest/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Jupyter](https://jupyter.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Promptflow](https://microsoft.github.io/promptflow/)
- [Langchain](https://langchain.com/)
- [Autogen](https://microsoft.github.io/autogen/)
