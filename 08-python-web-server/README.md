# Introduction to FastAPI and Uvicorn

This folder contains the code for the web server using FastAPI and Uvicorn

## Instructions

1. Install the dependencies
```bash
pip install -r requirements.txt
```

2. Run the server
 ```bash
 uvicorn main:app --reload
 ```

3. Open the browser and go to `http://localhost:8000`


## Docker

1. Build the image
```bash
docker build -t fastapi-uvicorn .
```

2. Run the container
```bash
docker run -d --name fastapi-uvicorn -p 8000:8000 fastapi-uvicorn
```

3. Open the browser and go to `http://localhost:8000`

