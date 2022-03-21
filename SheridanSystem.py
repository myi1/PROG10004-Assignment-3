from Building import Building


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
        numBuildings = input('Enter the number of buildings: ')
        # If user input is numerical and is at least 1 or more then executre the following code
        if numBuildings.isdigit() and int(numBuildings) >= 1:
            buildingCount = 0  # Set counter variable to 0
            # Declare a while loop to run the following code while the count is less than the number provided by user
            while buildingCount < int(numBuildings):
                # Instantiate a Building object, set to the building variable
                building = Building()
                # get the Building List
                BuildingsList = self.getBuildList()
                # Add the newly created building to the building list
                BuildingsList.append(building)
                # Set the BuildingList variable attribute value
                self.setBuildList(BuildingsList)
                # Iterate the count
                buildingCount += 1
