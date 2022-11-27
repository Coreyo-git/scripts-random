from pytube import Playlist
import os

# output folder for songs
musicOutputPath = './songs_output/'
musicFolderExists = os.path.exists(musicOutputPath)

# set playlist to youtube url of playlist
pl = Playlist(
    "https://www.youtube.com/playlist?list=PLwAGF46BaS2sjniZX4dviRW5gwTPAsp66")

# Checks if the folder exists, crates if not
def checkMusicOutputExists():
    if not musicOutputPath:
        os.makedirs(musicOutputPath)

# Downloads the playlist as audio
def download(pl):
    songs_downloaded = 0
    # loop through each video in playlist and download only audio
    for video in pl.videos:
        songs_downloaded += 1
        # stores the song output directory with the current song title as a string
	# checks if the current song is not already downloaded
	# if current song doesn't exist download as mp4 audio only
        current_song = str(video.title)+".mp4"
        if not os.path.isfile(musicOutputPath+current_song):
            print("Downloading: #", songs_downloaded, current_song)
            video.streams.filter(
                only_audio=True).first().download(musicOutputPath)

checkMusicOutputExists()
download(pl)
