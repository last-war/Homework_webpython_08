import pika
from model2 import Contact

import json

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def send_ad(id: str):
    conts = Contact.objects(pk=id)
    for cur in conts:
        cur.update(ad_send=True)


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    send_ad(message['id'])
    print(f" [x] Done: {message['id']}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='email_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
