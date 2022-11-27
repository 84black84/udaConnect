# Docker commands

## To build the web application
docker build -t udaconnect_persons_api .

## Run the web application locally
docker run -d -p 5003:5003 udaconnect_persons_api