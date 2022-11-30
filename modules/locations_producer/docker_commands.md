# Docker commands

## To build the web application
docker build -t udaconnect_locations_producer .

## Run the web application locally
docker run -d udaconnect_locations_producer

## To connect a running container to an existing user-defined bridge (udaconnect-net)
docker network connect udaconnect-net 88e9833fab3f

## Tag image
docker tag udaconnect_locations_producer 84black84/udaconnect_locations_producer:latest

## Push image
docker push 84black84/udaconnect_locations_producer:latest