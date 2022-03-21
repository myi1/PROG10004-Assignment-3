
class SheridanSystem:
    def __init__(self):
        self._noOfBuild = 0
        self._buildList = []

    def getNoOfBuild(self):
        return self._noOfBuild

    def setNoOfBuild(self, newNoOfBuild):
        self._noOfBuild = newNoOfBuild

    def getBuildList(self):
        return self._buildList

    def setBuildList(self, newBuildList):
        self._buildList = newBuildList

    def run(self):
        # Ask user how many buildings
        numBuildings = input('Enter the number of buildings:')
        # If user input is numerical and is at least 1 or more then executre the following code
        if numBuildings.isdigit() and int(numBuildings) >= 1:
            buildingCount = 0
