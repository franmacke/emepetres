import tkinter as tk
from .view import MainScreen


class Application:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Media Downloader")
        self.current_screen = MainScreen(self.root)

    def run(self):
        self.current_screen.render()
        self.root.mainloop()        