import datetime
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9093')

try:

    for _ in range(10_000):

        the_dt = str(datetime.datetime.utcnow())

        val = f"Count: {_} at {the_dt}".encode(encoding='utf8')

        producer.send(topic="KafkaExplored", value=val)

    producer.close()

except Exception as ex:

    print(ex)