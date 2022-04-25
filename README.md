# Dyson Desktop Client

An application that allows you to control a Dyson Fan from desktop. (Work in Progress)

## Table of contents
* [About](#about)
* [Technologies](#technologies)
* [Reverse Engineering Setup](#Reverse-Enginnering-Setup)
* [How It Works](#how-it-works)
* [Data Explaination](#data-explaination)
* [Running The Code Yourself](#running-the-code-yourself)
* [To-do](#to-do)
* [Thoughts on this project.](thoughts-on-this-project-&-what-i've-learned)

## About.
Allows you to control your Dyson Fan through your PC.

## Technologies.
### Languages: 
- Python 3.10+

### Libaries Used:
- [paho.mqtt.client](https://pypi.org/project/paho-mqtt/) - Library that enables applications to connect to a MQTT Broker. (in this case, the fan itself.)

## Reverse Enginnering Setup.
To start with I tried a few different apps on my phone to see what information is being sent. However, these apps seemed to create a virtual network. This resulted in the information being encrypted and routed through Dyson's AWS service. It may have been possible to do this method if you had root access on your phone and used a slightly different setup but my current phone's bootloader is locked so I'm not able to try.

The next thing I tried was using my laptop as a hotspot. I connected my phone to my local network through my laptop and used wireshark. This worked and allowed me to see what was being sent.
I was able to see it uses MQTT to communicate.

## How It Works.
MQTT is a publish and subscribe system. Devices publish messages on a specific topic. All devices that are subscribed to that topic receive the message. 
There are 4 topics we can subscribe to: 
-Current
-Software
-Connection
-Faults

## Data Explaination: 
### STATE
| Abbreviations  | Values | Meaning |
| ------------- | ------------- | ------------- |
| ercd    | I've only seen NONE  | Error Code |
| ffoc | ON , OFF | Sets the fan’s diffused mode on or off |
| fmod | ON, OFF, AUTO | Sets the fan to on, off or automatically maintain air quality and temperature |
| fnsp | 0 – 10 | Sets the fan speed.  Must have 4 digits. We can use rjust(4,'0') to pad |the data with zero's. (1 = 0001, 10 = 0010) |
| hmax | (x)°C | sets the heating temperature. The fan itself displays as Celsius. However, we need to send the data as Kelvin. The formula for that is (c + 273.15). We also need to round it. This is because Kelvin scale does not use the degree symbol. Kelvin is an absolute scale based on absolute 0 while Celsius is based on the properties of water. It then is multiplied by 10. |
| hmod | HEAT, OFF | sets the mode to either heating or cooling (off) |
| nmod | ON, OFF | Sets the fan’s night mode on or off | 
| oson | ON, OFF | Sets the fan’s oscillation on or off |
|sltm | 4 digits required | Sets the timer, data is sent in minutes |

### SENSOR DATA
| Abbreviations  | Values | Meaning |
| ------------- | ------------- | ------------- |
| hact    | 0000 - 0100   | Humidity as a percentage |
| pact    | 0000 - 0009   | Dust in the room  |
| sltm    | OFF OR Max time value(?)   | Sleep Timer |
| tact    | 0000 - ????   | Temperature in Kelvin |
| vact    | 0001 - 0009   | Air quality/organic compounds |


## Running the code yourself.
There are 4 pieces of information you need for your own device. I'll update how to get this later. 
They are:

-USERNAME = ''

-PASSWORD = ''

-HOST = '' 

-PORT = 1883 (default unencrypted port)

-IDENTIFIER = '455'

## To-do:
- Document the rest of the data
- Add reactive approach to handling data driven events (Fan change information)
- Add GUI
- Update documentation
- Refactor

## Thoughts on this project.
Coming Soon