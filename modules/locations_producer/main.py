import grpc
import time
import json
import location_pb2
import location_pb2_grpc
from concurrent import futures
from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
import logging

"""
    Creates a grpc server which can accept requests that include information for a new location object 
    for a particular person. Then create a message to a kafka item out of the received new location information.
"""

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("locations-producer")

TOPIC_NAME = 'locations'
KAFKA_SERVER = ['kafka']

def create_kafka_topic():
    """
        Creates a new 'locations' topic if it does not already exist.
    """
    consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER)
    topics = consumer.topics()
    if (len(topics) == 0 or 'locations' not in topics):
        logger.info("The 'locations' kafka topic will now be added in the topics list.")
        ## create new topic
        admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_SERVER)
        topic_list = []
        topic_list.append(NewTopic(name="locations", num_partitions=1, replication_factor=1))
        admin_client.create_topics(new_topics=topic_list, validate_only=False)

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
            logger.info('ready to send a message to kafka topic')
            create_kafka_topic()
            # send message to kafka topic
            producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
            kafka_data = json.dumps(request_value).encode()
            producer.send(TOPIC_NAME, kafka_data)
            producer.flush()
        except Exception as exception:
            logger.error(exception)
        finally:
            return location_pb2.LocationMessage(**request_value)


# Initialize the gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

logger.info("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)