#Work in progress!
from model import Model
from view import View
from controller import Controller
from mqtt_client import MQTT

import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #Using the MVC architectural pattern.
        # Any changes to UI data should come from the controller and the data should be based of what the MQTT broker (in our case the fan) sends. 
        # For example changing the fan speed. If we have a slider to do this, we will take the users input, However we should *never* update the fan speed model data. That data should only ever be updated from the f
        model = Model()
        view  = View(self)
        mqtt_client = MQTT()

        controller = Controller(model,view,mqtt_client)
        
        mqtt_client.set_controller(controller)
        view.set_controller(controller)

if __name__ == '__main__' :
    app = App()
    app.mainloop()