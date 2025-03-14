import paho.mqtt.client as mqtt
# broker details:
broker = "test.mosquitto.org"
port = 1883
topic = "/student_group/light_control"

# message callback
def on_message(client, userdata,message):
    command = message.payload.decode()
    if command == "ON":
        print("💡 ON")
    elif command == "OFF":
        print("⚡")
client = mqtt.Client()
client.on_message = on_message
client.connect(broker,port)
client.subscribe(topic)
print("Waiting for messages: ")
client.loop_forever()
