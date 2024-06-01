from src.model import Downloader
from threading import Thread

class DownloaderController:
    def __init__(self) -> None:
        self.downloader = Downloader()

    def handle(self, url, audio_var, video_var, on_download_complete):

        if audio_var.get():             
            task1 = Thread(target=self.downloader.download_media, args=(url, "audio", on_download_complete))           
            task1.start()

        if video_var.get():
            task2 = Thread(target=self.downloader.download_media, args=(url, "video"))
            task2.start()
        

        
