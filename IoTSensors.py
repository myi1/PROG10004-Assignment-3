class IoTSensors:
    # Define IoTSensors class which is a general sensor class
    def __init__(self):
        self._posX = 0
        self._posY = 0
        self._noDays = 0
        self._avgRead = 0

    # Accessor Methods
    def getPosX(self):
        return self._posX

    def getPosY(self):
        return self._posY

    def getNoDays(self):
        return self._noDays

    def getAvgRead(self):
        return self._avgRead

    # Mutator Methods
    def setPosX(self, newPosX):
        self._posX = newPosX

    def setPosY(self, newPosY):
        self._posY = newPosY

    def setNoDays(self, newNoDays):
        self._noDays = newNoDays

    def setAvgRead(self, newAvgRead):
        self._avgRead = newAvgRead

    # Other Methods
    def sensorPos(self):
        return

    def sensorReadings(self):
        return

    def computeAvg(self):
        return
