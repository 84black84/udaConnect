from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import UnknownTopicOrPartitionError
from kafka.admin import KafkaAdminClient, NewTopic

## Send a text message to a kafka topic
# producer = KafkaProducer(bootstrap_servers='localhost:9092')
# producer.send('items', b'another python test!!')
# producer.flush()


## list the exiting topics
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'])
topics = consumer.topics()
print(topics)

if (len(topics) == 0 or 'items' not in topics):
    print('items topic will now be added in the topics list')
    ## create new topic
    admin_client = KafkaAdminClient(bootstrap_servers=["localhost:9092"])
    topic_list = []
    topic_list.append(NewTopic(name="items", num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
    

def delete_topics(topic_names):
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=["localhost:9092"])
        admin_client.delete_topics(topics=topic_names)
        print("Topic Deleted Successfully")
    except UnknownTopicOrPartitionError as e:
        print("Topic Doesn't Exist")
    except  Exception as e:
        print(e)

topics = consumer.topics()
print(topics)

# delete_topics(topics)