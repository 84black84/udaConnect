from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import UnknownTopicOrPartitionError
from kafka.admin import KafkaAdminClient, NewTopic

'''
    Contains various helper methods to interact with Kafka server
'''

def send_test_text_message_to_kafka_locations_topic():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('locations', b'kafka producer in Python - test')
    producer.flush()

def print_all_existing_kafka_topics():
    '''
        listing the exiting kafka topics
    '''
    consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'])
    topics = consumer.topics()
    print(topics)


def delete_all_kafka_topics():
    try:
        consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'])
        topics = consumer.topics()
        admin_client = KafkaAdminClient(bootstrap_servers=["localhost:9092"])
        admin_client.delete_topics(topics=topics)
        print("Topic Deleted Successfully")
    except UnknownTopicOrPartitionError as e:
        print("Topic Doesn't Exist")
    except  Exception as e:
        print(e)
        
def create_kafka_topic():
    consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'])
    topics = consumer.topics()
    if (len(topics) == 0 or 'locations' not in topics):
        print("The 'locations' kafka topic will now be added in the topics list.")
        ## create new topic
        admin_client = KafkaAdminClient(bootstrap_servers=["localhost:9092"])
        topic_list = []
        topic_list.append(NewTopic(name="locations", num_partitions=1, replication_factor=1))
        admin_client.create_topics(new_topics=topic_list, validate_only=False)

# print_all_existing_kafka_topics()
# delete_all_kafka_topics()
# create_kafka_topic()
# print_all_existing_kafka_topics()
send_test_text_message_to_kafka_locations_topic()
