# URL Downloader by Suchada Nilthuean.
# Python & Kivy

import kivy
kivy.require('2.3.0')
from kivy.app import App
from kivy.lang import Builder
# Load .kv file
Builder.load_file('url_downloader.kv')

# Layout
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        return URL_Downloader()

class URL_Downloader(BoxLayout):
    pass




if __name__ == '__main__':
    MyApp().run()