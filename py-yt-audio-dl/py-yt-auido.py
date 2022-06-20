import os
from pytube import Playlist

songsOutputPath = './songs_output'
songsFolderExists = os.path.exists(songsOutputPath)
playlistURL = 'https://www.youtube.com/playlist?list=INPUT_LIST'

# Checks if the folder exists, crates if not
def checkOutputExists():
	if not songsFolderExists:
		os.makedirs(songsOutputPath)

# Downloads the playlist as audio
def download(playlist):
  # Tracks the download #
  download_number = 1
  # set playlist to youtube url of playlist
  playlist = Playlist(playlistURL)
  
  #loop through each video and download only audio
  for video in playlist.videos:
    video.streams.filter(only_audio=True).first().download(songsOutputPath)
    print('Video Download #',download_number, video.title)
    download_number += 1
    
checkOutputExists()
download(playlistURL)