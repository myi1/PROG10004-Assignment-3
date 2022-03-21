class IoTSensors:

    def __init__(self):
        self._posX = 0
        self._posY = 0
        self._noDays = 0
        self._avgRead = 0

    def getPosX(self):
        return self._posX

    def getPosY(self):
        return self._posY

    def getNoDays(self):
        return self._noDays

    def getAvgRead(self):
        return self._avgRead

    def setPosX(self, newPosX):
        self._posX = newPosX

    def setPosY(self, newPosY):
        self._posY = newPosY

    def setNoDays(self, newNoDays):
        self._noDays = newNoDays

    def setAvgRead(self, newAvgRead):
        self._avgRead = newAvgRead
