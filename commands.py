import datetime
import json

# The data sent for each action (turning on, fan speed, heating temp etc) all use the same format with the only change being the data in the data key.
# We create a Parent class with this template and all the child classes have their own implementation of it with the added data + the value that will be passed in.

class Commands:
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

    def publish(self):
        print(self.publish_template)
        self.publish_template['time'] = self.get_time()
        return json.dumps(self.publish_template, indent=2)

    #On, Off or AUTO.
    #Data fmod.
    #FAN = ON | OFF = OFF | AUTO = AUTO.
    # Auto mode automatically maintains air quality and temperature.
    def set_state(self,value):
        publish_data = self.publish_template.copy()
        publish_data['data']['fmod'] = value.upper()
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)
    
    #Heating or cooling.
    #Data hmod.
    #HEAT = Heating | OFF = Cooling.
    def set_mode(self, value):
        publish_data = self.publish_template.copy()
        publish_data['data']['hmod'] = value.upper()
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)
        
    #Fan speed. 
    #Data fnsp.
    #4 digits 0 to 10. Must have 4 digits. We can use rjust(4,'0') to pad the data with zero's. 1 = 0001 | 10 = 0010.
    def set_speed(self, value):
        publish_data = self.publish_template.copy()
        publish_data['data']['fnsp'] = value.rjust(4,'0')
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)
        

    #Heating Temperature.
    #Data hmax.
    #The fan itself displays as Celsius. However, we need to send the data as Kelvin. The formula  for that is (c + 273.15). We also need to round it.
    #This is because Kelvin scale does not use the degree symbol. Kelvin is an absolute scale based on absolute 0 while Celsius is based on the properties of water. It then is multiplied by 10.
    def set_temp(self, value):
        publish_data = self.publish_template.copy()
        publish_data['data']['hmax'] = round((int(value) + 273.15) * 10)
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)
        

    #Timer
    #Data sltm
    #4 digits required. Data is sent in minutes.
    def set_timer(self, value):
        publish_data = self.publish_template.copy()
        publish_data['data']['sltm'] = value.rjust(4,'0')
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)

    #Oscillation.
    #Data oson.
    #ON = ON | OFF = OFF.
    def set_osci(self, value):
        publish_data = self.publish_template.copy()
        publish_data['data']['oson'] = value
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)

    #Night Mode
    #Data nmod
    #ON = ON | OFF = OFF.
    def set_nmod(self, value):
        publish_data = self.publish_template.copy()
        publish_data['data']['nmod'] = value
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)

    #Diffused Mode
    #Data ffoc
    # OFF = diffused mode on | ON = diffused mode off
    def set_diffused(self, value):
        publish_data = self.publish_template.copy()
        publish_data['data']['ffoc'] = value
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)

    def get_current_state(self):
        publish_data = {
            'mode-reason' : 'LAPP',
            'time' : '',
            'msg' : 'REQUEST-CURRENT-STATE'
        }
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)

    def get_env_state(self):
        publish_data = {
            'mode-reason' : 'LAPP',
            'time' : '',
            'msg' : 'REQUEST-ENVIRONMENTAL-CURRENT-SENSOR-DATA'
        }
        publish_data['time'] = self.get_time()
        return json.dumps(publish_data,indent=2)
    
    def get_help(self, value):
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



