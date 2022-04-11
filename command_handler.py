import datetime
import json
import secrets


# The data sent for each action (turning on, fan speed, heating temp etc) all use the same format with the only change being the data in the data key.
# We create a Parent class with this template and all the child classes have their own implementation of it with the added data + the value that will be passed in.
class publish_data:
    def __init__(self):
        self.publish_template = {
            'data' : {
            },
            'mode-reason' : 'LAPP',
            'time' : '',
            'msg' : 'STATE-SET'
        }
    def get_time(self):
        date = datetime.datetime.utcnow()
        return date.strftime('%y-%m-%d') + 'T' + date.strftime('%H:%M:%S') + 'Z'

#class to get the current state of the fan. 
class request_current_state():
    def __init__(self):
        self.publish_template = {
            'mode-reason' : 'LAPP',
            'time' : '',
            'msg' : 'REQUEST-CURRENT-STATE'
        }
    def get_time(self):
        date = datetime.datetime.utcnow()
        return date.strftime('%y-%m-%d') + 'T' + date.strftime('%H:%M:%S') + 'Z'

    def publish(self):
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template, indent=2)

#On, Off or AUTO.
#Data fmod.
#FAN = ON | OFF = OFF | AUTO = AUTO.
# Auto mode automatically maintains air quality and temperature.
class state(publish_data):
    def __init__(self):
        super().__init__()

    def publish(self, value):
        self.publish_template['data']['fmod'] = value.upper()
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template, indent=2)

#Heating or cooling.
#Data hmod.
#HEAT = Heating | OFF = Cooling.
class mode(publish_data):
    def __init__(self):
        super().__init__()

    def publish(self, value):
        self.publish_template['data']['hmod'] = value.upper()
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template,indent=2)

#Fan speed. 
#Data fnsp.
#4 digits 0 to 10. Must have 4 digits. We can use rjust(4,'0') to pad the data with zero's. 1 = 0001 | 10 = 0010.
class speed(publish_data):
    def __init__(self):
        super().__init__()

    def publish(self, value):
        self.publish_template['data']['fnsp'] = value.rjust(4,'0')
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template,indent=2)

#Heating Temperature.
#Data hmax.
#The fan itself displays as Celsius. However, we need to send the data as Kelvin. The formula  for that is (c + 273.15). We also need to round it.
#This is because Kelvin scale does not use the degree symbol. Kelvin is an absolute scale based on absolute 0 while Celsius is based on the properties of water. It then is multiplied by 10.
class temp(publish_data):
    def __init__(self):
        super().__init__()

    def publish(self, value):
        self.publish_template['data']['hmax'] = round((int(value) + 273.15) * 10)
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template,indent=2)

#Timer
#Data sltm
#4 digits required. Data is sent in minutes.
class timer(publish_data):
    def __init__(self):
        super().__init__()

    def publish(self, value):
        self.publish_template['data']['sltm'] = value.rjust(4,'0')
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template,indent=2)

#Oscillation.
#Data oson.
#ON = ON | OFF = OFF.
class osci(publish_data):
    def __init__(self):
        super().__init__()

    def publish(self, value):
        self.publish_template['data']['oson'] = value
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template,indent=2)

#Night Mode
#Data nmod
#ON = ON | OFF = OFF.
class nmode(publish_data):
    def __init__(self):
        super().__init__()

    def publish(self, value):
        self.publish_template['data']['nmod'] = value
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template,indent=2)

#Diffused Mode
#Data ffoc
# OFF = diffused mode on | ON = diffused mode off
class diffused(publish_data):
    def __init__(self):
        super().__init__()

    def publish(self, value):
        self.publish_template['data']['ffoc'] = value
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template,indent=2)

class command_help():
    def get_info(self, value):
        command_info = {
            'state' : 'Turns the fan ON, OFF or sets it to AUTO mode. Values: FAN = ON | OFF = OFF | AUTO = AUTO.',
            'mode' : 'Turns on Heating or Cooling. Values: HEAT = Heating | OFF = Cooling.',
            'speed' : 'Changes the Fan Speed. Values: 0 to 10.',
            'temp' : 'Sets the Heating temperature. Value in Celsius.',
            'timer' : 'Sets the Timer to turn off. Value in minutes.',
            'osci' : 'Turns the Oscillation ON or OFF. Values ON | OFF.',
            'night' : 'Turns Night Mode ON or OFF. Values ON | OFF.',
            'diffused' : 'Turns Diffused Mode ON or OFF. Values:  OFF = diffused mode on | ON = difused mode off.'
        }
        if value in command_info.keys():
            print(command_info[value])
        else:
            print("Unknown command")



