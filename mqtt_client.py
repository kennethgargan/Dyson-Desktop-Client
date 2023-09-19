import paho.mqtt.client as mqtt
import secrets
import json

topic_publish = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/command"
topic_current = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/status/current"
topic_software = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/status/software"
topic_connection = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/status/connection"
topic_faults = f"{secrets.IDENTIFIER}/{secrets.USERNAME}/status/faults"

class MQTT:
    def __init__(self, clientid=None):
        self.client = mqtt.Client(clientid)
        self.client.on_message = self.mqtt_on_message
        self.client.on_connect = self.mqtt_on_connect
        self.client.on_publish = self.mqtt_on_publish
        #self.client.on_subscribe = self.mqtt_on_subscribe
        self.client.username_pw_set (secrets.USERNAME, secrets.PASSWORD)
        self.client.connect(secrets.HOST, port = secrets.PORT, keepalive = 60 )
        self.client.loop_start()

    def mqtt_on_message(self,client,userdata,msg):
        payload = json.loads(msg.payload.decode("utf-8"))
        print(f"message payload: {payload}")
        if payload['msg'] == "CURRENT-STATE":
            self.controller.update_fan_data(payload['product-state'])

        if payload['msg'] == "ENVIRONMENTAL-CURRENT-SENSOR-DATA":
            self.controller.update_env_data(payload['data'])

    def mqtt_on_connect(self,client, userdata, flags, response_code):
        if response_code == 0:
            print("Connected. ")
            self.client.subscribe(topic_current)
            self.client.subscribe(topic_software)
            self.client.subscribe(topic_connection)
            self.client.subscribe(topic_faults)
        else:
            print("Failed")
    def mqtt_on_publish(self,client,userdata,msg,retain=True):
        pass

    def publish_message(self,data):
        print(data)
        self.client.publish(topic_publish,data)

    def loop_stop(self):
        self.client.loop_stop()

    def set_controller(self,controller):
        self.controller = controller
    
