import RPi.GPIO as GPIO  #GPIOにアクセスするライブラリをimportします。                                          
import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("subscribe")
    GPIO.output(15,GPIO.HIGH)
    time.sleep(5.0)
    GPIO.output(15,GPIO.LOW)


broker = "localhost"
port = 1883
topic = "test/topic"

GPIO.setmode(GPIO.BCM)                       
GPIO.setup(15,GPIO.OUT)                               
GPIO.output(15,GPIO.LOW)

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port, 60)
client.subscribe(topic)
client.loop_forever()
