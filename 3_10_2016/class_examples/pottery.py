class Pottery():
    def __init__(self, input_name, input_bake_temperature, input_description=None):
        self._name = input_name
        self._bake_temperature = input_bake_temperature
        self._description = input_description
        self._bake_status = "unbaked"

    def mark_as_baked(self):
        self._bake_status = "baked"

    def get_name(self):
        return self._name

    def get_bake_temperature(self):
        return self._bake_temperature   

    def get_description(self):
        return self._description

    def get_bake_status(self):
        return self._bake_status

