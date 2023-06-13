import os
import requests
import shutil
from pytube import YouTube as TY


def save_thumbnail(url: str, image_title: str) -> None:
    """ saves video thumbnail """

    req = requests.get(url, stream=True)
    if req.status_code != 200:
        print('Video thumbnail  could not be download')
        return

    with open(image_title, 'wb') as img:
        shutil.copyfileobj(req.raw, img)
    print('image successfully downloaded')


def download_video(video_url: str):
    video = TY(video_url)
    video_title = video.title

    print(f'Downloading video: {video_title}')
    new_directory = f'./downloads/videos/{video_title}'
    
    if os.path.exists(new_directory):
        print("You've downloaded this file in the past...,\nif not delete folder with the video title")
        return

    os.mkdir(new_directory)
    os.chdir(new_directory)

    print('downloading....')
    save_thumbnail(video.thumbnail_url, f'{video_title}.jpg')
    #if video.caption_captions.has_key('en'):
    #    video.captions.get_by_language_code('en').generate_srt_captions()
    video.streams.filter(progressive=True, file_extension='mp4', res='720p').first().download()

    print('download complete....')
    









if __name__ == "__main__":
    # video_url = "https://youtu.be/KiNBhjeMI4Y?list=PLdHg5T0SNpN0ygjV4yGXNct25jY_ue70U"
    video_url = input("Enter video url: ")
    download_video(video_url)

# TODO:  include resolution selection
# TODO:  include 
