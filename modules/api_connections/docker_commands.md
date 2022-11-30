# Docker commands

## To build the web application
docker build -t udaconnect_connections_api .

## Run the web application locally
docker run -d -p 5001:5001 udaconnect_connections_api

## To connect a running container to an existing user-defined bridge (udaconnect-net)
docker network connect udaconnect-net a4d22e8b6d52