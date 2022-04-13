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

    def update_env_data(self,payload: dict) -> None:
        for key,value in payload.items():
            if key in self.env_data:
                self.env_data[key] == value
