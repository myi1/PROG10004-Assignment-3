class Building:

    def __init__(self):
        self._noOfSensors = 0
        self._listOfSensors = []
        self._buildName = ''

    def getNoOfSensors(self):
        return self._noOfSensors

    def getListOfSensors(self):
        return self._listOfSensors

    def getBuildName(self):
        return self._buildName

    def setnoOfSensors(self, newNoOfSensors):
        self._noOfSensors = newNoOfSensors

    def setListOfSensors(self, newListofSensors):
        self._listOfSensors = newListofSensors

    def setBuildName(self, newBuildName):
        self._buildName = newBuildName
