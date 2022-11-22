import grpc
import time
import json
import location_pb2
import location_pb2_grpc
from concurrent import futures
from kafka import KafkaProducer

"""
    Creates a grpc server which can accept requests that include information for a new location object 
    for a particular person. Then create a message to a kafka item out of the received new location information.
"""

TOPIC_NAME = 'items'
KAFKA_SERVER = ['localhost:9092']

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        
        print('Received a message.')

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        
        print(request_value)
        
        try:
            print('ready to send a message to kafka topic')
            # send message to kafka topic
            producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
            kafka_data = json.dumps(request_value).encode()
            producer.send(TOPIC_NAME, kafka_data)
            producer.flush()
        except Exception as exception:
            print(exception)
        
        finally:
            return location_pb2.LocationMessage(**request_value)


# Initialize the gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)