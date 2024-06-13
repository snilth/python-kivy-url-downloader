# URL Downloader by Suchada Nilthuean.
# Python & Kivy

import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()