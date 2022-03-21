from IoTSensors import IoTSensors
import random


class Co2Sensors(IoTSensors):

    def __init__(self):
        super.__init__()
        self._co2Levels = 0

    def getco2Levels(self):
        return self._co2Levels

    def setCo2Levels(self, newCo2Levels):
        self._co2Levels = newCo2Levels

    def sensorPos(self):
        self._posX = format(random.uniform(0, 100), '.2f')
        self._posY = format(random.uniform(0, 100), '.2f')

    def sensorReadings(self, sensorNum):
        dayReading = input(
            'Enter the CO2 Reading (PPM) for Day {0}'.format(sensorNum))
        if dayReading.isdigit():
            self.setCo2Levels(int(dayReading))
