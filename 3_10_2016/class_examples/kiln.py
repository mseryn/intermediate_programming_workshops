class Kiln():
    def __init__(self, input_temperature=78):
        self._contents = []
        self._temperature = input_temperature

    def add_pottery(self, added_pottery):
        for pottery in added_pottery:
            self._contents.append(pottery)
            if pottery.get_bake_temperature() >= self._temperature:
                pottery.mark_as_baked()

    def change_temperature(self, new_temperature):
        self._temperature = new_temperature
        for pottery in self._contents:
            if pottery.get_bake_temperature() >= self._temperature:
                pottery.mark_as_baked()

    def get_temperature(self):
        return self._temperature

    def get_contents(self, state=None):
        if state:
            pottery_of_specified_state = [x for x in self._contents if x.get_bake_status() == state]
            return pottery_of_specified_state
        return self._contents

    def list_contents(self, state=None):
        if state:
            pottery_of_specified_state = [x for x in self._contents if x.get_bake_status() == state]
            for pottery in pottery_of_specified_state:
                if pottery.get_description():
                    print("%s: bake temperature=%i, description=%s" %(pottery.get_name(), pottery.get_bake_temperature(), pottery.get_description()))
                else:
                    print("%s: bake temperature=%i" %(pottery.get_name(), pottery.get_bake_temperature()))
        else:
            for pottery in self._contents:
                if pottery.get_description():
                    print("%s: bake temperature=%i, description=%s" %(pottery.get_name(), pottery.get_bake_temperature(), pottery.get_description()))
                else:
                    print("%s: bake temperature=%i" %(pottery.get_name(), pottery.get_bake_temperature()))
