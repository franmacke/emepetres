import tkinter as tk
from src.controller import DownloaderController
from .IScreen import IScreen

class MainScreen(IScreen):
    def __init__(self, root) -> None:
        self.root = root
        self.downloader = DownloaderController()
        self.download_button = None
    
    def on_download_complete(self):
        self.download_button["state"] = "normal"

    def handle_download_press(self, url_entry, audio_var, video_var):
        self.downloader.handle(url_entry, audio_var, video_var, self.on_download_complete)
        self.download_button["state"] = "disabled"

    def render(self):
        url_label = tk.Label(self.root, text="Enter YouTube URL:")
        url_label.pack(pady=10)

        url_entry = tk.Entry(self.root, width=50)
        url_entry.pack()

        audio_var = tk.IntVar()
        video_var = tk.IntVar()

        audio_checkbox = tk.Checkbutton(
            self.root, 
            text="Download Audio", 
            variable=audio_var, 
        )
        audio_checkbox.pack()

        video_checkbox = tk.Checkbutton(
            self.root, 
            text="Download Video", 
            variable=video_var, 
        )
        video_checkbox.pack()

        self.download_button = tk.Button(
            self.root, 
            text="Download", 
            command=lambda: self.handle_download_press(url_entry.get(), audio_var, video_var)
        )
        
        self.download_button.pack(pady=10)

        download_status = tk.StringVar()

        status_label = tk.Label(self.root, textvariable=download_status)
        status_label.pack()