import yt_dlp
import mover


source_directory = r'path\to\where\you\want\to\save\the\videos' # Add videos directory
thumbnail_directory = r'path\to\where\you\want\to\save\the\thumbnails' # Add thumbnails directory
playlist = 'link to playlist' # Add playlist (or video) link

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
    ydl.download('link_to_playlist')

mover.move_files_to_thumbnail_directory(source_directory, thumbnail_directory)
