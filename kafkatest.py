from kafka import KafkaConsumer

consumer = KafkaConsumer('stocks')
for msg in consumer:
	print("Received a message: " + str(msg))

