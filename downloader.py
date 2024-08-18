import yt_dlp
import mover
from pytube import Playlist
 

video_directory = r'path\to\where\you\want\to\save\the\videos' # Add videos directory
thumbnail_directory = r'path\to\where\you\want\to\save\the\thumbnails' # Add thumbnails directory
playlist = 'link to playlist' # Add playlist (or video) link

p = Playlist(playlist)

ydl_opts = {
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslangs': ['en-orig','en'],
    'writethumbnail' : True,
    'paths': {
        'home': video_directory,
        'thumbnail' : thumbnail_directory 
               }, 
    'ffmpeg_location' : 'C:/yt-dlp',
    'embedsubtitles': True,  # Embed subtitles into the video
    'postprocessors': [{
        'key': 'FFmpegEmbedSubtitle',  # Use FFmpeg to embed subtitles
    }],
}

for video_url in p.video_urls:
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print(f"Error during download: {e}")

mover.move_files_to_thumbnail_directory(video_directory, thumbnail_directory)
