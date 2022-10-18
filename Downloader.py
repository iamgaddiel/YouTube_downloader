import os
import requests
from pytube import YouTube as TY



class Downloader():
    def __init__(self, url, video_type: str, is_playlist: bool=False ) -> None:
        pass

    def video_downloader(self, video_url: str):
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
        if video.caption_captions.has_key('en'):
            video.captions.get_by_language_code('en').generate_srt_captions()
        video.streams.filter(progressive=True, file_extension='mp4', res='720p').first().download()

        print('download complete....')
    
    def playlist_downloader(self, video_url: str):
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
        if video.caption_captions.has_key('en'):
            video.captions.get_by_language_code('en').generate_srt_captions()
        video.streams.filter(progressive=True, file_extension='mp4', res='720p').first().download()

        print('download complete....')
    
    
