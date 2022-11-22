from kafka import KafkaConsumer
# from kafka.admin import KafkaAdminClient, NewTopic

TOPIC_NAME = 'items'

consumer = KafkaConsumer(TOPIC_NAME)
print('consumer started listening ->')
for message in consumer:
    print(message)