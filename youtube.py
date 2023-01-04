import pytube
#the location you want to save
save = r"C:\Users\--\Documents"
#video file to be downloaded
link = input('Enter the link you want to download')

yt = pytube.YouTube(link)
yt.streams.filter(progressive = True,
file_extension = "mp4").first().download(save)

#tite of file being downloaded
print(yt.title)

#gif
from moviepy.editor import *
clip = VideoFileClip("m_Trim.mp4")
clip = clip.subclip(0, 3)
clip.write_gif("mygif.gif")
