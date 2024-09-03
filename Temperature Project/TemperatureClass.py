celsius_reps = ['c', 'C', 'Celsius']
farenheit_reps = ['f', 'F', 'Farenheit']
kelvin_reps = ['k', 'K', "Kelvin"]

class Temperature:
    def __init__(self,temperature_type, value):
        if temperature_type in farenheit_reps :
            temperature_type = "Farenheit"
        elif temperature_type in celsius_reps:
            temperature_type = "Celsius"
        elif temperature_type in kelvin_reps:
            temperature_type = "Kelvin"
        self.temperature_type = temperature_type
        self.value = value
    def convert(self, target_type):
        if self.temperature_type == target_type:
            return Temperature(self.temperature_type, self.value)
        if self.temperature_type == "Farenheit" and target_type in celsius_reps:
            new_value = (self.value -32)*5/9
            return Temperature(target_type, new_value)
        if self.temperature_type == "Celsius" and target_type in farenheit_reps:
            new_value = (self.value*(9/5))+32
            return Temperature(target_type, new_value)
        if self.temperature_type == "Farenheit" and target_type in kelvin_reps:
            new_value = (self.value -32)*(5/9) + 273.15
            return Temperature(target_type, new_value)
        if self.temperature_type == "Celsius" and target_type in kelvin_reps:
            new_value = (self.value + 273.15)
            return Temperature(target_type,new_value)
        if self.temperature_type == "Kelvin" and target_type in celsius_reps:
            new_value = self.value - 273.15
            return Temperature(target_type, new_value)
        if self.temperature_type == "Kelvin" and target_type in farenheit_reps:
            new_value = (9/5)*(self.value -273.15)+32
            return Temperature(target_type, new_value)
    def __repr__(self):
        print('The new temperature is:', self.value, self.temperature_type)


