from yt_dlp import YoutubeDL
from src.Settings import YTDL_OPTIONS_AUDIO, YTDL_OPTIONS_VIDEO

class Downloader:
    def __init__(self) -> None:
        self.is_downloading = False

    def download_media(self, url, type, callback):

        self.is_downloading = True
        downloader = YoutubeDL(YTDL_OPTIONS_AUDIO if type == "audio" else YTDL_OPTIONS_VIDEO)
    
        info = downloader.extract_info(url, download=True)
        
        self.is_downloading = False
        
        title = info.get("title")
        url = info.get("url")
        duration = info.get("duration")
        thumbnail = info.get("thumbnails")[0]["url"]
        website_url = info.get("webpage_url")

        print("-----------------")
        print(f"Title: {title}")
        print(f"Duration: {duration}")
        print(f"Thumbnail: {thumbnail}")
        print(f"Website URL: {website_url}")
        print("-----------------")

        callback()

        return title, url, duration, thumbnail, website_url
        

