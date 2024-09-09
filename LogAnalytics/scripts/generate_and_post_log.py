import datetime
import random
import json
from kafka import KafkaProducer
from time import sleep

# Kafka configuration
KAFKA_TOPIC = 'logs'
KAFKA_BROKER = 'workshop-kafka:9092'  # Change to your Kafka broker address

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize as JSON
)

# Define two sets of variables
methods = ['CONNECT','DELETE','GET','HEAD','OPTIONS','PATCH','POST','PUT','TRACE']
response_codes = [100,200,300,400,500]
pages = ['/','page1','page2','page3','page4','page5','page6','page7','page8','page9','page10']

# Function to generate random message
def generate_random_message():
    message = {
        'ip': '192.168.198.92',
        'timestamp': datetime.datetime.now().isoformat() ,
        'method': random.choice(methods),
        'uri': random.choice(pages),
        'protocol': 'HTTPS',
        'version': '1.2',
        'response_code': random.choice(response_codes),
        'time': random.randint(10, 5000),
        'domain': 'www.test.com'
    }
    return message

# Function to send random message to Kafka
def send_message_to_kafka():
    while True:
        message = generate_random_message()
        print(f'Sending message: {message}')
        producer.send(KAFKA_TOPIC, message)
        producer.flush()  # Ensure the message is sent
        sleep(1)  # Sleep for 2 seconds before sending the next message

if __name__ == "__main__":
    try:
        send_message_to_kafka()
    except KeyboardInterrupt:
        print("Stopped producing messages.")
    finally:
        producer.close()
