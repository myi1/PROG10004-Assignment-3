from Building import Building
import re


class SheridanSystem:  # Define the SheridanSystem class, which holds the data about the buildings as well as methods to run the simulation
    def __init__(self):
        self._noOfBuild = 0
        self._buildList = []
        self._buildingNumQuery = '---------------------------------------------------------\nEnter the number of buildings: '
        self._buildingNameQuery = 'Enter the building name: '

    # Accessor Methods
    def getNoOfBuild(self):
        return self._noOfBuild

    def getBuildList(self):
        return self._buildList

    # Mutator Methods
    def setNoOfBuild(self, newNoOfBuild):
        self._noOfBuild = newNoOfBuild

    def setBuildList(self, newBuildList):
        self._buildList = newBuildList

    def setBuildingNumQuery(self, newBuildingNumQuery):
        self._buildingNumQuery = newBuildingNumQuery

    def setBuildingNameQuery(self, newBuildingNameQuery):
        self._buildingNameQuery = newBuildingNameQuery

    # Define the run method, which runs the primary simulation and outputs the results
    def run(self):
        # Define a boolean variable that determines the wording of the query given to the user, based on whether they gave a valid entry on the first attempt
        validEntry = False
        # Declare a while loop to run the following code while the condition is valid
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

            else:  # If the user inputs an invalid response, print an error response, change the user query wording and while loop will repeat
                print('\nInvalid Entry')
                self.setBuildingNumQuery('Re-Enter the number of buildings: ')

            for building in self._buildList:  # Define a loop based on the number of building objects created
                print('Building {0}'.format(
                    self._buildList.index(building) + 1))
                # Define a boolean variable that determines the wording of the query given to the user, based on whether they gave a valid entry on the first attempt
                validBuildingName = False
                # Declare a while loop to run the following code while the condition is valid
                while not validBuildingName:
                    # Request name from the user
                    buildName = input(self._buildingNameQuery)
                    # Error validation to check building name is in correct format
                    rex = re.compile("^[A-Z]-Building$")

                    if rex.match(buildName):  # If correct format...
                        # Change boolean variable value to True to stop loop from repeating
                        validBuildingName = True
                        # Use mutator method to revert query wording back to original
                        self.setBuildingNameQuery('Enter the building name: ')
                        # Use mutator method to assign value of building name
                        building.setBuildName(buildName)
                        validNumSensors = False  # Define a boolean variable that determines the wording of the query given to the user, based on whether they gave a valid entry on the first attempt
                        building.setNoOfSensors(
                            input('Enter the number of sensors deployed accross Sheridan Campus: '))
                        # Declare a while loop to run the following code while the condition is valid
                        while not validNumSensors:
                            # Error validation to check if user input is a numerical and at least 1 or more
                            if building._noOfSensors.isdigit() and int(building._noOfSensors) >= 1:
                                count = 1  # Counting variable
                                # Declare a while loop to run the following code while the count is less than the number provided by user
                                while count <= int(building._noOfSensors):
                                    print('Sensor {0}'.format(count))
                                    # Create sensor object using createSensors method in Building class
                                    sensor = building.createSensors()
                                    count += 1  # Iterate the count
                                    validNumSensors = True  # Change value of boolean variable to true to end loop
                            else:
                                # If the user inputs an invalid response, print an error response, change the user query wording and while loop will repeat
                                print('\nInvalid Entry')
                                building.setNoOfSensors(
                                    input('Re-Enter the number of sensors deployed accross Sheridan Campus: '))

                    else:
                        # If the user inputs an invalid response, print an error response, change the user query wording and while loop will repeat
                        print('\nInvalid Entry')
                        self.setBuildingNameQuery(
                            'Re-Enter the building name: ')
            # Output section
            for building in self._buildList:  # For each building in the buildings list....
                # Prints the building name
                print(building)

                # For each sensor in the current building...
                for sensor in building._listOfSensors:
                    # Prints the sensor output
                    print('***************\nSensor {0}'.format(
                        building._listOfSensors.index(sensor)+1))
                    print('x: {0}\ny: {1}'.format(sensor._posX, sensor._posY))
                    # For each day CO2Readings were taken for current sensor...
                    for days in range(sensor._noDays):
                        # Prints that day's CO2 reading
                        print('Day {0} {1} PPM'.format(
                            days+1, sensor._co2Levels[days]))
                    print('Average Reading(s): {0} PPM\n***************\n\n'.format(
                        sensor._avgRead))  # Prints the Average CO2 Readings for current sensor
