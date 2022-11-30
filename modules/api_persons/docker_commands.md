# Docker commands

## To build the web application
docker build -t udaconnect_persons_api .

## Run the web application locally
docker run -d -p 5003:5003 udaconnect_persons_api

## To connect a running container to an existing user-defined bridge (udaconnect-net)
docker network connect udaconnect-net c43aadd57114

## Tag image
docker tag udaconnect_persons_api 84black84/udaconnect_persons_api:latest

## Push image
docker push 84black84/udaconnect_persons_api:latest