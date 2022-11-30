# Docker commands

## To build the web application
docker build -t udaconnect_connections_api .

## Run the web application locally
docker run -d -p 5001:5001 udaconnect_connections_api

## To connect a running container to an existing user-defined bridge (udaconnect-net)
docker network connect udaconnect-net 0fc3258ce6d6

## Tag image
docker tag udaconnect_connections_api 84black84/udaconnect_connections_api:latest

## Push image
docker push 84black84/udaconnect_connections_api:latest