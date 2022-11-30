from kafka import KafkaConsumer
import ast
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.udaconnect.schemas import LocationSchema
from app.udaconnect.models import Location
from geoalchemy2.functions import ST_Point
import logging

'''
    Creates a kafka consumer for the topic 'Locations' which listens to new messages constantly.
'''

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger("kafka locations topic consumer")

def create_location(location):
    '''
        Inserts a location object into the database by using the Sql Alchemy framework
    '''
    validation_results = LocationSchema().validate(location)
    if validation_results:
        logger.error(f"Unexpected data format in payload: {validation_results}")
    else: 
        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        session.add(new_location)
        session.commit()
        session.close()

SQLALCHEMY_DATABASE_URI = f"postgresql://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
TOPIC_NAME = 'locations'

engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = Session(engine)
consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers='kafka')
logger.info("'Locations' topic Kafka consumer started listening...")

for message in consumer:
    logger.debug(message.value)
    logger.debug('')
    location = ast.literal_eval(message.value.decode("UTF-8"))
    logger.debug(location)
    logger.debug('')
    logger.debug(type(location))
    create_location(location)