import secrets
import paho.mqtt.client as mqtt
import json
import pprint

# There are 5 topics to subscribe to:
topic_publish = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/command"
topic_current = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/status/current"
topic_software = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/status/software"
topic_connection = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/status/connection"
topic_faults = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/status/faults"

def create_client():
    client = mqtt.Client(protocol = mqtt.MQTTv311)
    client.username_pw_set (secrets.USERNAME, secrets.PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.connect(secrets.HOST, port = secrets.PORT, keepalive = 60 )
    client.loop_start
    print("Client Created")
    return client

def on_connect (client, userdata, flags, response_code):
    if response_code == 0:
        print("Connected. ")
        client.subscribe(topic_current)
        client.subscribe(topic_software)
        client.subscribe(topic_connection)
        client.subscribe(topic_faults)
    else:
        print("Failed")

def on_message (client, userdata, msg):
    update = json.loads(msg.payload)
    # print(msg.topic)
    # pprint.pprint(update)

    if update['msg'] == 'CURRENT-STATE':
        pprint.pprint(update['product-state']['tilt'])

def on_publish(client,userdata, msg, retain=True):
    pass

def publish_message(client,data):
    client.publish(topic_publish,data)
    
