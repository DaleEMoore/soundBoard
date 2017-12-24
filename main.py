#!/usr/bin/env python3

# Sound Board

import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout


class aScreen(GridLayout):

    # TODO; Calls to auth() fail with "TypeError: auth() takes 1 positional argument but 2 were given"
    def auth(self, instance):
        print("User: " + str(self.username.text))
        if self.username.text == "Hendricko":
            print("self.username == " + str(self.username.text))
            content = Button(text='Howdy! Close me!')
            popup = Popup(title="success",
                          content=content,
                          size=(100, 100),
                          size_hint=(0.3, 0.3),
                          auto_dismiss=False)
            content.bind(on_press=popup.dismiss)
            popup.open()

    # I've tried, and failed:(
    class Foo():
        def initUI(self):
            self.add_widget(Button(text="Auth User and Password", on_press=self.auth))

    def callback(self, instance, value):
        print('My button <%s> state is <%s>' % (instance, value))

    def __init__(self, **kwargs):
        super(aScreen, self).__init__(**kwargs)
        self.cols = 2
        self.row = 2
        self.add_widget(Label(text='User Name (try Hendricko)'))
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

        print("MyApp.build Button")
        button1 = Button(text="Push button for picture and sound")
        #button1 = self.add_widget(Button(text="Push button for picture and sound"))
        button1.bind(on_press=self.callback)

        print("MyApp.build Label")
        self.add_widget(Label(text='Hello world label'))
        print("build done")


class MyApp(App):

    def build(self):
        return aScreen()

if __name__ == '__main__':
    print("Main code in python main.py script.")
    MyApp().run()
