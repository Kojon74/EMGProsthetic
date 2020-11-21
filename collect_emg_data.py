'''
Environment name: prosthetic_venv
'''
from gpiozero import SmoothedInputDevice

emg_sensor = SmoothedInputDevice(4, queue_len = 1)
emd_data = []

while(True):
    emg_data.append(emg_sensor.value())