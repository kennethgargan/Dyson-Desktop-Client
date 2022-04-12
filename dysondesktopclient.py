#Work in progress!
import mqtt_client
import command_handler
import command
import time

if __name__ == '__main__' :
    commands = command_handler()
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
    client = mqtt_client.create_client()
    time.sleep(2)
    print("Ready to use.")
    print("Supported commands:  " + str([*command_list.keys()]))
    while True:
        user_input = input()

        if ":" in user_input:
            user_input = user_input.split(':')
            if user_input[0] in command_list.keys():
                mqtt_client.publish_message(client,command_list[user_input[0]](user_input[1]))
        elif user_input == "current":
            mqtt_client.publish_message(client,commands.get_current_state())
        elif user_input[0] == 'disconnect':
            break
    client.loop_stop()
