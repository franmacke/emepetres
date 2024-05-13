from yt_dlp import YoutubeDL
import sys
import tkinter as tk

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
    'outtmpl': 'output/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s',
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
    'outtmpl': 'output/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s',
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


root = tk.Tk()
root.title("YouTube Downloader")

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack()

audio_var = tk.IntVar()
video_var = tk.IntVar()

def handle_checkbox(var1, var2):
    if var1.get():
        var2.set(False)
    else:
        var2.set(True)

audio_checkbox = tk.Checkbutton(
    root, 
    text="Download Audio", 
    variable=audio_var, 
    command=lambda: handle_checkbox(audio_var, video_var)
)
audio_checkbox.pack()

video_checkbox = tk.Checkbutton(
    root, 
    text="Download Video", 
    variable=video_var, 
    command=lambda: handle_checkbox(audio_var, video_var)
)
video_checkbox.pack()

download_button = tk.Button(
    root, 
    text="Download", 
    command=lambda: download_media(url_entry.get(), YTDL_OPTIONS_AUDIO if audio_var.get() else YTDL_OPTIONS_VIDEO)
)
download_button.pack(pady=10)

download_status = tk.StringVar()
status_label = tk.Label(root, textvariable=download_status)
status_label.pack()

root.mainloop()
