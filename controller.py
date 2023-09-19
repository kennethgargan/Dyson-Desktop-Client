from mqtt_client import MQTT
from commands import Commands
import time

class Controller:
    def __init__(self,model,view,mqtt_client):
        self.model = model
        self.view = view
        self.mqtt_client = mqtt_client
        self.mqtt_client = mqtt_client

    def ping(self):
        print("Ping!")

    #Remove when UI is working.
    def ready(self):
        commands = Commands()
        command_list = {
            'state': commands.set_state,
            'mode' : commands.set_mode,
            'speed': commands.set_speed,
            'temp': commands.set_temp,
            'timer': commands.set_timer,
            'osci': commands.set_osci,
            'night': commands.set_nmod,
            'diffused': commands.set_diffused,
            'current':commands.get_current_state,
            'help':commands.get_help
        }
        time.sleep(2)
        print("Ready to use.")
        print("Supported commands:  " + str([*command_list.keys()]))
        while True:
            user_input = input()
            if ":" in user_input:
                user_input = user_input.split(":")
                self.mqtt_client.publish_message(command_list[user_input[0]](user_input[1]))
            else:
                self.mqtt_client.publish_message(command_list[user_input]())
    
    def update_fan_data(self,payload):
        self.model.update_fan_data(payload)
    
    def update_env_data(self, payload):
        self.model.update_env_data(payload)
