import yt_dlp
import json
from pytube import Playlist
import ffmpeg
import shutil
import os
import mover


source_directory = r'path\to\where\you\want\to\save\the\videos' 
thumbnail_directory = r'path\to\where\you\want\to\save\the\thumbnails' 


ydl_opts = {
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslangs': ['en-orig','en'],
    'writethumbnail' : True,
    'paths': {
        'home': source_directory,
        'thumbnail' : thumbnail_directory 
               }, 
    'ffmpeg_location' : 'C:/yt-dlp',
    'embedsubtitles': True,  # Embed subtitles into the video
    'postprocessors': [{
        'key': 'FFmpegEmbedSubtitle',  # Use FFmpeg to embed subtitles
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download('https://www.youtube.com/playlist?list=PLHX1Fyul-dSs6nzZ7uAI2wHnd8NnN9EMr')

mover.move_files_to_thumbnail_directory(source_directory, thumbnail_directory)
