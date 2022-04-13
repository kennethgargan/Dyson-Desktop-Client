#Work in progress!
from model import Model
from commands import Commands
from mqtt_client import MQTT
import time


if __name__ == '__main__' :
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
    #client = mqtt_client.create_client()
    model = Model()
    mqtt = MQTT(model)
    time.sleep(2)
    print("Ready to use.")
    print("Supported commands:  " + str([*command_list.keys()]))

    while True:
        user_input = input()
        if ":" in user_input:
            user_input = user_input.split(":")
            mqtt.publish_message(command_list[user_input[0]](user_input[1]))
        else:
            mqtt.publish_message(command_list[user_input]())