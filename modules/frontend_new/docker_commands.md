# Docker commands

## To build the web application
docker build -t udaconnect_frontend .

## Run the web application locally
docker run -d -p 3001:3001 udaconnect_frontend

## To connect a running container to an existing user-defined bridge (udaconnect-net)
docker network connect udaconnect-net ed535666589e