import pytube
# video_url = 'https://www.youtube.com/watch?v=EXTvJVyER3w' # paste here your Youube videos' url
video_url = 'https://www.youtube.com/watch?v=YDNA9VYyOME' # paste here your Youube videos' url



youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('C:/Atom-Temp/homework/Youtube/') # path, where to video download.