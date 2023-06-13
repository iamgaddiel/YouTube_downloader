import os
import requests
import shutil
from pytube import YouTube as TY
from pytube import Playlist


class YoutubeDownloader():
    download_url = ""

    def __init__(self, url) -> None:
        self.download_url = url
        print('downloading process initiated....')

    def __save_thumbnail(url: str, image_title: str) -> None:
        """ saves video thumbnail """

        req = requests.get(url, stream=True)
        if req.status_code != 200:
            print('Video thumbnail  could not be download')
            return

        with open(image_title, 'wb') as img:
            shutil.copyfileobj(req.raw, img)
        print('image successfully downloaded')

    def download_video(self):
        video = TY(self.download_url)

        print(f'Downloading video: {video.title}')
        video_download_directory = f'./downloads/videos/{video.title}'

        if os.path.exists(video_download_directory):
            print(
                "You've downloaded this file in the past...,\nif not delete folder with the video title")
            return

        os.mkdir(video_download_directory)
        os.chdir(video_download_directory)

        self.__save_thumbnail(video.thumbnail_url, f'{video.title}.jpg')
        if video.caption_captions.has_key('en'):
            video.captions.get_by_language_code('en').generate_srt_captions()
        video.streams.filter(
            progressive=True, file_extension='mp4', res='720p').first().download()

        print('video download complete....')
        print(f'See your video at {video_download_directory}')


    def download_playlist(self, resolution: str = '720p'):
        playlist = Playlist(self.download_url)

        playlist_title = playlist.title

        print(f'Downloading Playlist: {playlist_title}')
        playlist_directory = f'./downloads/playlists/{playlist_title}'

        if os.path.exists(playlist_directory):
            print(
                "You've downloaded this playlist in the past...,\nif not delete folder with the video title")
            return

        os.mkdir(playlist_directory)
        os.chdir(playlist_directory)

        self.__save_thumbnail(playlist.thumbnail_url, f'{playlist}.jpg')
        for video in playlist.videos:
            video.streams.filter(
                progressive=True, file_extension='mp4', res=resolution).first().download()

        print('download complete....')
        print(f'See your playlist at {playlist_directory}')

    def audio_downloader():
        pass

    def download_audio_playlist(self):
        pass


if __name__ == "__main__":
    url = input("Enter YouTube url: ")

    if url == "":
        print("Enter youtube url")

    try:
        yt_object = YoutubeDownloader(url) 
        
        VIDEO = "v"
        PLAYLIST = "p"

        response = str(input("What do you want to dowload(v/p): "))

        if response == VIDEO:
            yt_object.download_video()
        
        elif response == PLAYLIST:
            yt_object.download_playlist()
        
        else:
            print("Invalid input")
        yt_object = YoutubeDownloader(url) 
        # questions
        VIDEO = "v"
        PLAYLIST = "p"

        response = str(input("What do you want to dowload(v/p): "))

        if response == VIDEO:
            yt_object.download_video()
        
        elif response == PLAYLIST:
            yt_object.download_playlist()
        
        else:
            print("Invalid input")

    except:
        print("An Error occured, could not download video")
