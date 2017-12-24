#!/usr/bin/env python3

# Sound Board

import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

#I'm trying to bind the following function to a Button in Kivy.

# here is my whole code

from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__()
        #super(ImageButton, self).__init__(**kwargs)

class aScreen(GridLayout):
    def auth(self):
        print(self.username)
        if self.username == "Hendricko":
            print("self.username == Hendricko")
            popup = Popup(title="success",
                          content=Label(text="Howdy !"),
                          size=(100, 100),
                          size_hint=(0.3, 0.3),
                          auto_dismiss=False)
            popup.open()

    # I've tried

    class Foo():
        def initUI(self):
            self.add_widget(Button(text="Auth User and Password", on_press=self.auth))

    # but this doesn't work. What am I doing wrong?

    def callback(self, instance):
    #    def callback(self, instance, value):
        print('My button')
        print('instance <%s>' % (instance))
        #print('value <%s>' % (value))
        #print('My button <%s> state is <%s>' % (instance, value))

    def __init__(self, **kwargs):
        super(aScreen, self).__init__(**kwargs)
        self.cols = 2
        self.row = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.hello = Button(text="Push button for authorization", on_press=self.auth)
        self.add_widget(self.hello)

        # TODO: kivy button picture thumbnail
        # https://kivy.org/docs/api-kivy.uix.button.html
        # TODO; kivy show picture when button pushed
        # TODO; kivy play sound when button pressed
        # https://kivy.org/docs/examples/gen__demo__pictures__main__py.html


        print("MyApp.build Button")
        button1 = Button(text="Push button for picture and sound",
                         on_press=lambda a: self.callback(self),
                         )
        #self.hello = Button(text="hello", on_press=lambda a: self.auth())
        #button1 = Button(text="Push button for picture and sound", image="pearl.jpg")
        # "/home/dalem/PycharmProjects/soundBoard/pearl.jpg"
        # "/home/dalem/PycharmProjects/soundBoard/judyMomDale.jpg"
        #button1 = self.add_widget(Button(text="Push button for picture and sound"))
        #button1.bind(on_press=self.callback)
        self.add_widget(button1)

        print("ImageButton")
        button2 = ImageButton(text="elPush moi",
                         on_press=lambda a: self.callback(self),
                         )
        self.add_widget(button2)

        print("MyApp.build Label")
        self.add_widget(Label(text='Hello world label'))
        print("build done")


class MyApp(App):

    def build(self):
        return aScreen()

if __name__ == '__main__':
    print("Main code in python main.py script.")
    MyApp().run()
