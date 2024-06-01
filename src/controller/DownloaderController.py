from src.model import Downloader

class DownloaderController:
    def __init__(self) -> None:
        self.downloader = Downloader()

    def handle(self, url, audio_var, video_var):
        if audio_var.get():
            self.downloader.download_media(url, "audio")

        if video_var.get():
            self.downloader.download_media(url, "video")
