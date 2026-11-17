# Lab 3: Containerizing the Student Management API

## Objective

Package the Lab 2 Student Management API in a Docker container, run it in GitHub Codespaces, check its endpoints and logs, and publish the image to Docker Hub.

## Tools

- FastAPI and Uvicorn
- Docker
- GitHub Codespaces
- Docker Hub

## Docker configuration

The `Dockerfile` uses the official Python 3.15 slim image, installs packages from `requirements.txt`, copies the API files into the image, and starts Uvicorn on port 8000. The `.dockerignore` file excludes Git data, Python cache files, and virtual environments from the build.

## Build and run

The image was built with:

`docker build -t student-management-api:1.0 .`

The container was run with port 8000 forwarded and the environment variable `APP_ENV=lab3`.

## API checks

| Check | Result |
|---|---|
| Swagger documentation at `/docs` | Opened |
| `POST /students` | 201 Created; student ID 1 |
| `GET /students` | 200 OK; student record returned |
| Container logs | Showed successful POST and GET requests |
| `APP_ENV` inside container | `lab3` |

## Docker Hub

The image was tagged and pushed as:

`meendi/student-management-api:1.0`

The push completed successfully. The image was also visible in the Docker Hub repositories list.

## Conclusion

The Student Management API was packaged as a Docker image, run and checked in GitHub Codespaces, and published to Docker Hub.