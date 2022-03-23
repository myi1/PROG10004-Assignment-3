from IoTSensors import IoTSensors
import random


class Co2Sensors(IoTSensors):
    # Define Co2Sensors class which inherits attributes from IoTSensors class

    def __init__(self):
        super().__init__()  # Initialize inheritable attributes from IoTSensors
        self._co2Levels = []  # Add new attribute specific to Co2Sensors

    # Accessor Methods
    def getCo2Levels(self):
        return self._co2Levels

    # Mutator Methods
    def setCo2Levels(self, newCo2Levels):
        self._co2Levels = newCo2Levels

    # Define sensorPos method which assigns an X & Y coordianate value to the sensor
    def sensorPos(self):
        posX = format(random.uniform(0, 100), '.2f')
        self.setPosX(posX)
        posY = format(random.uniform(0, 100), '.2f')
        self.setPosY(posY)

    # Define sensorReradings method which asks the user for the days CO2 Reading and stores that information
    def sensorReadings(self, sensorNum):
        validCo2Reading = False  # Define a boolean variable that determines the wording of the query given to the user, based on whether they gave a valid entry on the first attempt
        dayReading = input(
            'Enter the CO2 Reading (PPM) for Day {0}: '.format(sensorNum))  # Ask user for input
        while not validCo2Reading:  # Declare a while loop to run the following code while the condition is valid
            if dayReading.isdigit():  # Error validation to check if user input is a numerical
                co2Levels = self.getCo2Levels()  # use Accessor method to get list of co2 levels
                # append new reading to the list
                co2Levels.append(int(dayReading))
                # use Mutator method to assign the new list to the object's attribute
                self.setCo2Levels(co2Levels)
                validCo2Reading = True  # Change boolean varialble to end the loop
            # If the user inputs an invalid response, print an error response, change the user query wording and while loop will repeat
            else:
                print('\nInvalid Entry')
                dayReading = input(
                    'Re-Enter the CO2 Reading (PPM) for Day {0}: '.format(sensorNum))
    # Define computeAvg method which takes a list of readings and gets the average in the required format.

    def computeAvg(self, listReadings):
        self.setAvgRead(format((sum(listReadings) / len(listReadings)), '.2f'))
