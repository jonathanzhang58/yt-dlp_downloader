import yt_dlp
import mover
from pytube import Playlist
 

source_directory = r'test' 
thumbnail_directory = r'thumbnails' 
playlist = 'https://www.youtube.com/playlist?list=PLHX1Fyul-dSsLdOui2FGoEny5hq6azP6m'

p = Playlist(playlist)

for i in p:
    print(i)