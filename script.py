from src.Application import Application

class Script:
    def __init__(self) -> None:
        self.app = Application()

    def run(self):
        self.app.run()


if __name__ == "__main__":
    script = Script()
    script.run()