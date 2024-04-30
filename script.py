from yt_dlp import YoutubeDL
import sys

YTDL_OPTIONS_AUDIO = {
    "format": "bestaudio/best",
    "extractaudio": True,
    "outtmpl": "%(title)s.%(ext)s",
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

YTDL_OPTIONS_VIDEO = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "outtmpl": "%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": False,
    "nocheckcertificate": True,
    "ignoreerrors": True,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": False,
    "default_search": "auto",
    "source_address": "0.0.0.0",
}

def download_media(song, options):
    downloader = YoutubeDL(options)
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
    song_url = sys.argv[1]
    download_audio = sys.argv[2].lower() == 'audio'
    
    if download_audio:
        download_media(song_url, YTDL_OPTIONS_AUDIO)
    else:
        download_media(song_url, YTDL_OPTIONS_VIDEO)
