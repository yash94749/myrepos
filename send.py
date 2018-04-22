#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

channel.queue_declare(queue='RAMRAM')

channel.basic_publish(exchange='',
                      routing_key='RAMRAM',
                      body='Jai Shriram!')
print(" [x] Sent 'Jai ShriRam!'")
connection.close()


