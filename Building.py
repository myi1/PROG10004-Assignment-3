from Co2Sensors import Co2Sensors


class Building:
    # Building class which holds all information for each building, specifically the sensor objects

    def __init__(self):
        self._noOfSensors = 0
        self._listOfSensors = []
        self._buildName = ''
        self._numDaysQuery = 'Enter the number of days for the sensor(s) to collect CO2 levels: '

    # Accessor Methods
    def getNoOfSensors(self):
        return self._noOfSensors

    def getListOfSensors(self):
        return self._listOfSensors

    def getBuildName(self):
        return self._buildName

    # Mutator Methods
    def setNoOfSensors(self, newNoOfSensors):
        self._noOfSensors = newNoOfSensors

    def setListOfSensors(self, newListofSensors):
        self._listOfSensors = newListofSensors

    def setBuildName(self, newBuildName):
        self._buildName = newBuildName

    def setNumDaysQuery(self, newNumDaysQuery):
        self._numDaysQuery = newNumDaysQuery

    # Define the createSensors methods, which creates Sensor objects and gets readings
    def createSensors(self):
        sensor = Co2Sensors()  # Instatiate Co2Sensor object
        sensor.sensorPos()  # Run sensorPos method from Co2Sensors class
        validNumDays = False  # Define a boolean variable that determines the wording of the query given to the user, based on whether they gave a valid entry on the first attempt
        while not validNumDays:  # Declare a while loop to run the following code while the condition is valid
            # Ask user for input on number of days
            numDays = input(self._numDaysQuery)
            # Error validation to check if user input is a numerical and at least 1 or more
            if numDays.isdigit() and int(numDays) >= 1:
                sensor.setNoDays(int(numDays))  # Set value of days
                validNumDays = True  # Change value of boolean variable to stop loop repeating
                count = 1  # Counting variable
                while count <= sensor.getNoDays():  # Define while loop to iterate while count is less than the user inputed # of days
                    # Runs the sensorReadings method from the Co2Sensors class
                    sensor.sensorReadings(count)
                    count += 1  # Iterate the count
                # After loop is complete, run computeAvg method from Co2Sensors class
                sensor.computeAvg(sensor._co2Levels)
                # Add sensor object to end of sensor list
                self._listOfSensors.append(sensor)
            # If the user inputs an invalid response, print an error response, change the user query wording and while loop will repeat
            else:
                print('\nInvalid Entry')
                self.setNumDaysQuery(
                    'Re-Enter the number of days for the sensor(s) to collect CO2 levels: ')

    def __str__(self):  # Define str return value in required format
        return '\n\n****************************\n\nThis is for Building: {0}\n\n\n****************************'.format(self._buildName)
