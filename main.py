# URL Downloader by Suchada Nilthuean.
# Python & Kivy

import kivy
kivy.require('2.3.0')
from kivy.app import App
from kivy.lang import Builder
# Load .kv file
Builder.load_file('url_downloader.kv')

# Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# Library
from pytube import YouTube

class URL_Downloader(BoxLayout):
    def download_video(self):
        try:
            url = self.ids.url_input.text
            yt = YouTube(url)
            video_stream = yt.streams.filter(file_extension='mp4')
            video_stream.get_highest_resolution().download(output_path='C:\HobbyProjects\python-kivy-url-downloader\Video_files')
        except Exception as e:
            print(f"Error : {e}")

    def download_audio(self):
        try:
            url = self.ids.url_input.text
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path='C:\HobbyProjects\python-kivy-url-downloader\Audio_files')
        except Exception as e:
            print(f"Error : {e}")

class URLDownloaderApp(App):
    def build(self):
        return URL_Downloader()

        


if __name__ == '__main__':
    URLDownloaderApp().run()