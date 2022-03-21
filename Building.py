from Co2Sensors import Co2Sensors


class Building:

    def __init__(self):
        self._noOfSensors = 0
        self._listOfSensors = []
        self._buildName = ''
        self._numDaysQuery = 'Enter the number of days for the sensor(s) to collect CO2 levels: '

    def getNoOfSensors(self):
        return self._noOfSensors

    def getListOfSensors(self):
        return self._listOfSensors

    def getBuildName(self):
        return self._buildName

    def setNoOfSensors(self, newNoOfSensors):
        self._noOfSensors = newNoOfSensors

    def setListOfSensors(self, newListofSensors):
        self._listOfSensors = newListofSensors

    def setBuildName(self, newBuildName):
        self._buildName = newBuildName

    def setNumDaysQuery(self, newNumDaysQuery):
        self._numDaysQuery = newNumDaysQuery

    def createSensors(self):
        sensor = Co2Sensors()
        sensor.sensorPos()
        validNumDays = False
        while not validNumDays:
            numDays = input(self._numDaysQuery)
            if numDays.isdigit() and int(numDays) >= 1:
                sensor.setNoDays(int(numDays))
                validNumDays = True
                count = 1
                while count <= sensor.getNoDays():
                    sensor.sensorReadings(count)
                    count += 1
                sensor.computeAvg(sensor._co2Levels)
                self._listOfSensors.append(sensor)

            else:
                print('\nInvalid Entry')
                self.setNumDaysQuery(
                    'Re-Enter the number of days for the sensor(s) to collect CO2 levels: ')

    def __str__(self):
        return '\n\n****************************\n\nThis is for Building: {0}\n\n\n****************************'.format(self._buildName)
