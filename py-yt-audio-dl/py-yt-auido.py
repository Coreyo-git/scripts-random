from pytube import Playlist

# set playlist to youtube url of playlist
pl = Playlist("https://www.youtube.com/playlist")

#loop through each video and download only audio
for video in pl.videos:
  stream = video.streams.filter(only_audio=True).first().download('./songs_output')
