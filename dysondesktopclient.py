#Work in progress!
import mqtt_client
import command_handler
import time

if __name__ == '__main__' :

    command_list = {
        'state': command_handler.state().publish,
        'mode' : command_handler.mode().publish,
        'speed': command_handler.speed().publish,
        'temp': command_handler.temp().publish,
        'timer' : command_handler.timer().publish,
        'osci': command_handler.osci().publish,
        'night': command_handler.nmode().publish,
        'diffused': command_handler.diffused().publish,
        'help':command_handler.command_help().get_info,
    }

    client = mqtt_client.create_client()
    time.sleep(2)
    print("Ready to use.")
    print("Supported commands:  " + str([*command_list.keys()]))
    
    while True:
        user_input = input().split(':')
        if user_input[0] == 'current':
            mqtt_client.publish_message(client,command_handler.request_current_state.publish(user_input[0]))
        elif user_input[0] in command_list.keys():
            mqtt_client.publish_message(client,command_list[user_input[0]](user_input[1]))
        elif user_input[0] == 'disconnect':
            break
    client.loop_stop()
