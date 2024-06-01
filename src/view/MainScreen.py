import tkinter as tk
from src.controller import DownloaderController
from .IScreen import IScreen

class MainScreen(IScreen):
    def __init__(self, root) -> None:
        self.root = root
        self.downloader = DownloaderController()

    def get_selection(self, audio_var, video_var):
        if audio_var.get():
            return "audio"
        elif video_var.get():
            return "video"
        else:
            return None
    
    # def handle_checkbox(self, var1, var2):
    #     if var1.get():
    #         var2.set(False)
    #     else:
    #         var2.set(True) 

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
            # command=lambda: self.handle_checkbox(audio_var, video_var)
        )
        audio_checkbox.pack()

        video_checkbox = tk.Checkbutton(
            self.root, 
            text="Download Video", 
            variable=video_var, 
            # command=lambda: self.handle_checkbox(audio_var, video_var)
        )
        video_checkbox.pack()

        download_button = tk.Button(
            self.root, 
            text="Download", 
            command=lambda: self.downloader.handle(url_entry.get(), audio_var, video_var)
        )
        
        download_button.pack(pady=10)

        download_status = tk.StringVar()
        status_label = tk.Label(self.root, textvariable=download_status)
        status_label.pack()

            