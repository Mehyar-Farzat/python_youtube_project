
from pytube import YouTube
def download_video(link):
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    try:
        stream.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the YouTube video URL:")
download_video(link)
