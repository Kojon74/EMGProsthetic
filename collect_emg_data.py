'''
Environment name: prosthetic_venv
'''
from gpiozero import SmoothedInputDevice

emg_sensor = SmoothedInputDevice(4, queue_len = 1)

while(True):
    emg_value = emg_sensor.value()