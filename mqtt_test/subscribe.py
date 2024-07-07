import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    message = message.payload.decode()
    print("Subscribe message : {}".format(message))


broker = "localhost"
port = 1883
topic = "test/topic"


client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port, 60)
client.subscribe(topic)
client.loop_forever()
