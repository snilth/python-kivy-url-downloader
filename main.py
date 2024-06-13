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

class MyApp(App):
    def build(self):
        return URL_Downloader()

class URL_Downloader(BoxLayout):
    def download(self):
        url = self.ids.url_input.text
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path='C:\HobbyProjects\python-kivy-url-downloader\Audio_files')



if __name__ == '__main__':
    MyApp().run()