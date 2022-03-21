from SheridanSystem import SheridanSystem


class Application:
    def start(self):
        sheridanSystem = SheridanSystem()
        sheridanSystem.run()


app = Application()
app.start()
