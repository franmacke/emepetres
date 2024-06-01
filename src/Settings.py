OUTPUT_DIR = "output"


YTDL_OPTIONS_AUDIO = {
    "format": "bestaudio/best",
    "extractaudio": True,
    'outtmpl': OUTPUT_DIR + '/audio/%(extractor)s-%(id)s-%(title)s.%(ext)s',
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
    'outtmpl': OUTPUT_DIR + '/video/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    # "outtmpl": "%(title)s.%(ext)s",
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
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }]
}