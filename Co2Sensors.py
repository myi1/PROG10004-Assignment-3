from IoTSensors import IoTSensors
import random


class Co2Sensors(IoTSensors):

    def __init__(self):
        super().__init__()
        self._co2Levels = []

    def getCo2Levels(self):
        return self._co2Levels

    def setCo2Levels(self, newCo2Levels):
        self._co2Levels = newCo2Levels

    def sensorPos(self):
        posX = format(random.uniform(0, 100), '.2f')
        self.setPosX(posX)
        posY = format(random.uniform(0, 100), '.2f')
        self.setPosY(posY)

    def sensorReadings(self, sensorNum):
        validCo2Reading = False
        dayReading = input(
            'Enter the CO2 Reading (PPM) for Day {0}: '.format(sensorNum))
        while not validCo2Reading:
            if dayReading.isdigit():
                co2Levels = self.getCo2Levels()
                co2Levels.append(int(dayReading))
                self.setCo2Levels(co2Levels)
                validCo2Reading = True
            else:
                print('\nInvalid Entry')
                dayReading = input(
                    'Re-Enter the CO2 Reading (PPM) for Day {0}: '.format(sensorNum))

    def computeAvg(self, listReadings):
        self.setAvgRead(format((sum(listReadings) / len(listReadings)), '.2f'))
