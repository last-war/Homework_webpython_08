import pika
import faker
from model2 import Contact

from datetime import datetime

import json

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='email_market', exchange_type='direct')
channel.queue_declare(queue='email_queue', durable=True)
channel.queue_bind(exchange='email_market', queue='email_queue')


def seed():
    fake_data = faker.Faker()
    for _ in range(0, 30):
        new_contact = Contact(fullname=fake_data.name(), email=fake_data.email())
        new_contact.born_date = fake_data.date()
        new_contact.save()


def main():
    contacts = Contact.objects()
    for contact in contacts:
        message = {
            "id": str(contact.id),
            "date": datetime.now().isoformat()
        }

        channel.basic_publish(
            exchange='email_market',
            routing_key='email_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
    connection.close()


if __name__ == '__main__':
    seed()
    main()
