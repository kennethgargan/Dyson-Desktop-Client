class Model:
    def __init__(self):
        self.fan_data = {
            "fmod" : "",
            "fnst" : "",
            "fnsp" : "",
            "qtar" : "",
            "oson" : "",
            "rhtm" : "",
            "filf" : "",
            "ercd" : "",
            "nmod" : "",
            "wacd" : "",
            "hmod" : "",
            "hmax" : "",
            "hsta" : "",
            "ffoc" : "",
            "tilt" : ""

        }
        self.env_data ={
            "tact" : "",
            "hact" : "",
            "pact" : "",
            "vact" : "",
            "sltm" : ""
        }
    
    def update_fan_data(self,payload):
        for key,value in payload.items():
            if key in self.fan_data:
                self.fan_data[key] = value
        self.get_fan_data()

    def update_env_data(self,payload):
        for key,value in payload.items():
            if key in self.env_data:
                self.env_data[key] = value
        self.get_env_data()

    def get_fan_data(self):
        print("---------")
        for key,value in self.fan_data.items():
            print(f"{key} : {value}")

    def get_env_data(self):
        print("---------")
        for key,value in self.env_data.items():
            print(f"{key} : {value}")