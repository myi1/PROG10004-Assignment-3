from Building import Building
import re


class SheridanSystem:
    def __init__(self):
        self._noOfBuild = 0
        self._buildList = []
        self._buildingNumQuery = '---------------------------------------------------------\nEnter the number of buildings: '
        self._buildingNameQuery = 'Enter the building name: '

    def getNoOfBuild(self):
        return self._noOfBuild

    def setNoOfBuild(self, newNoOfBuild):
        self._noOfBuild = newNoOfBuild

    def getBuildList(self):
        return self._buildList

    def setBuildList(self, newBuildList):
        self._buildList = newBuildList

    def setBuildingNumQuery(self, newBuildingNumQuery):
        self._buildingNumQuery = newBuildingNumQuery

    def setBuildingNameQuery(self, newBuildingNameQuery):
        self._buildingNameQuery = newBuildingNameQuery

    def run(self):
        validEntry = False
        while not validEntry:
            # Ask user how many buildings
            numBuildings = input(self._buildingNumQuery)
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
                    validEntry = True

            else:
                print('\nInvalid Entry')
                self.setBuildingNumQuery('Re-Enter the number of buildings: ')

            for building in self._buildList:
                print('Building {0}'.format(
                    self._buildList.index(building) + 1))

                validBuildingName = False
                while not validBuildingName:
                    buildName = input(self._buildingNameQuery)
                    rex = re.compile("^[A-Z]-Building$")

                    if rex.match(buildName):
                        validBuildingName = True
                        building.setBuildName(buildName)
                        validNumSensors = False
                        building.setNoOfSensors(
                            input('Enter the number of sensors deployed accross Sheridan Campus: '))
                        while not validNumSensors:
                            if building._noOfSensors.isdigit() and int(building._noOfSensors) >= 1:
                                count = 1
                                while count <= int(building._noOfSensors):
                                    print('Sensor {0}'.format(count))
                                    sensor = building.createSensors()
                                    count += 1
                                    validNumSensors = True
                            else:
                                print('\nInvalid Entry')
                                building.setNoOfSensors(
                                    input('Re-Enter the number of sensors deployed accross Sheridan Campus: '))

                    else:
                        print('\nInvalid Entry')
                        self.setBuildingNameQuery(
                            'Re-Enter the building name: ')

            for building in self._buildList:
                print(building)

                for sensor in building._listOfSensors:
                    print('***************\nSensor {0}'.format(
                        building._listOfSensors.index(sensor)+1))
                    print('x: {0}\ny: {1}'.format(sensor._posX, sensor._posY))
                    for days in range(sensor._noDays):
                        print('Day {0} {1} PPM'.format(
                            days+1, sensor._co2Levels[days]))
                    print('Average Reading(s): {0} PPM\n***************\n\n'.format(
                        sensor._avgRead))
