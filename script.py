from yt_dlp import YoutubeDL
import sys

YTDL_OPTIONS = {
    "format": "bestaudio/best",
    "extractaudio": True,
    "audioformat": "mp3",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": False,
    "nocheckcertificate": True,
    "ignoreerrors": True,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": False,
    "default_search": "auto",
    "source_address": "0.0.0.0",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def download_song(song):
    downloader = YoutubeDL(YTDL_OPTIONS)
    info = downloader.extract_info(song, download=True)
    
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

    return title, url, duration, thumbnail, website_url

if __name__ == "__main__":
    download_song(sys.argv[1])
