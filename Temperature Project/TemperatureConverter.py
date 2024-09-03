from TemperatureClass import Temperature
from pprint import pprint
print("Welcome to Temperature Converter!")
temperature_type = input("What unit of measurement are you using?")
degree_number = float(input("How many degrees is it?"))
target_type = input("What unit of measurement do you want to convert this to?")
original_temperature = Temperature(temperature_type, degree_number)
converted_temperature = original_temperature.convert(target_type)
converted_temperature.__repr__()