# Docker commands

## To build the web application
docker build -t udaconnect_locations_api .

## Run the web application locally
docker run -d -p 5002:5002 udaconnect_locations_api
