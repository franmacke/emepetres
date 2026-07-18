# Media Downloader App

A simple application that allows users to download audio and video content from popular platforms like YouTube, SoundCloud, and more. Just provide the link, and the app will download the content in either MP3 (audio) or MP4 (video) format.
Features:

- Download audio (MP3) or video (MP4) from supported platforms.
- Supports YouTube, SoundCloud, and other media platforms.
- Lightweight and easy to use interface.

Usage:

- Provide the link to the media you want to download.
- Select the format (Audio and/or Video).
- Download your file!

## Setup

Requires: Python 3.10+, Node.js (used by yt-dlp for YouTube extraction), and ffmpeg on PATH.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python script.py
```

Downloaded files land in `output/audio/` and `output/video/`.

## Build (optional, PyInstaller)

```bash
.venv/bin/pip install pyinstaller
.venv/bin/pyinstaller script.spec
```
