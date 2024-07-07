import paho.mqtt.client as mqtt
import time


broker = "localhost"
port = 1883
topic = "test/topic"


loop = 0
while True:
    
    message = "Hello! MQTT & counter is {}".format(loop)
    client = mqtt.Client()
    client.connect(broker, port, 60)
    client.publish(topic, message)
    client.disconnect()
    
    print("Publish message : {}".format(message))
    
    time.sleep(1)
    loop += 1
