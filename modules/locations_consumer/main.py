from kafka import KafkaConsumer

TOPIC_NAME = 'locations'

consumer = KafkaConsumer(TOPIC_NAME)
print('consumer started listening ->')
for message in consumer:
    print(message)