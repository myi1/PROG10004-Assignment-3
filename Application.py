from SheridanSystem import SheridanSystem


class Application:  # Defining the Application class
    # Define the start method which instantiates SheridanSystem class and runs it.
    def start(self):
        sheridanSystem = SheridanSystem()
        sheridanSystem.run()


app = Application()
app.start()
