from IoTSensors import IoTSensors
import random


class Co2Sensors(IoTSensors):

    def __init__(self):
        super.__init__()
        self._co2Levels = 0

    def sensorPos(self):
        self._posX = format(random.uniform(0, 100), '.2f')
        self._posY = format(random.uniform(0, 100), '.2f')
