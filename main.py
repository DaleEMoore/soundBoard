#!/usr/bin/env python2
# ! /usr/bin/env python3

# Sound Board

print("The start of everything.")

import kivy
print("kivy version " + str(kivy.__version__))
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.uix.popup import Popup
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

# From: https://stackoverflow.com/questions/33489143/kivy-image-as-button
class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__()
        #super(ImageButton, self).__init__(**kwargs)

    def on_press(self):
        print ('%s pressed' % str(self))
        pass

class aScreen(GridLayout):

    def auth(self, instance):
        print("User: " + str(self.username.text))
        if self.username.text == "Hendricko":
            content = Button(text='Howdy! Close me!')
            popup = Popup(title="success",
                          content=content,
                          size=(100, 100),
                          size_hint=(0.3, 0.3),
                          auto_dismiss=False)
            content.bind(on_press=popup.dismiss)
            popup.open()
        else:
            content = Button(text='Sorry, nope! Close me!')
            popup = Popup(title="failure",
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
        self.add_widget(Label(text='User Name (try Hendricko)'))
        self.username = TextInput(multiline=False, text="Hendricko")
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

        # Try https://stackoverflow.com/questions/26821651/kivy-how-to-make-an-image-act-like-a-button
        # https://kivy.org/docs/api-kivy.atlas.html for PNG instead of JPG?
        # TODO; Google "make a png for kivy button"
        # TODO; https://groups.google.com/forum/#!topic/kivy-users/tBZH1dJyz3M

        # This, kivy-logo-black-64.png, works in button1.py.
        # All these PNGs work in button1.py. Something else is wrong here.
        png2 = StringProperty("daleemoore.mooreworks.org/JoulesSB/BabyHeartbeat.png")
        #png2 = StringProperty("kivy-logo-black-64.png")
        button2 = ImageButton(text="elPushy moi",
                              background_normal=png2,
                              background_disabled_down=png2,
                              background_disabled_normal=png2,
                              background_down=png2,

                              # background_normal=StringProperty(
                              #    "atlas://home/dalem/PycharmProjects/soundBoard/daleemoore.mooreworks.org/JoulesSB/BabyHeartbeat.png"),

                              #"/home/dalem/PycharmProjects/soundBoard/daleemoore.mooreworks.org/JoulesSB/BabyHeartbeat.png"),

        #background_disabled_down=StringProperty(
                              #    "/home/dalem/PycharmProjects/soundBoard/daleemoore.mooreworks.org/JoulesSB/friday.png"),
                              #background_disabled_normal=StringProperty(
                              #    "/home/dalem/PycharmProjects/soundBoard/daleemoore.mooreworks.org/JoulesSB/fossilMuseum.png"),
                              #background_down=StringProperty(
                              #    "/home/dalem/PycharmProjects/soundBoard/daleemoore.mooreworks.org/JoulesSB/TeslaBottle.png"),

                              #background_disabled_down=StringProperty(
                              #    "atlas://home/dalem/PycharmProjects/soundBoard/daleemoore.mooreworks.org/JoulesSB/friday.png"),
                              #background_disabled_normal=StringProperty(
                              #    "atlas://home/dalem/PycharmProjects/soundBoard/daleemoore.mooreworks.org/JoulesSB/fosselMuseum.png"),
                              #background_down=StringProperty(
                              #    "atlas://home/dalem/PycharmProjects/soundBoard/daleemoore.mooreworks.org/JoulesSB/TeslaBottle.png"),
                              #background_normal=StringProperty(
                              #    "atlas://home/dalem/PycharmProjects/soundBoard/daleemoore.mooreworks.org/JoulesSB/BabyHeartbeat.png"),

                              #background_disabled_down="atlas://home/dalem/PycharmProjects/soundBoard/pearl.jpg",
                              #background_disabled_normal="atlas://home/dalem/PycharmProjects/soundBoard/pearl.jpg",
                              #background_down="atlas://home/dalem/PycharmProjects/soundBoard/pearl.jpg",
                              #background_normal="atlas://home/dalem/PycharmProjects/soundBoard/pearl.jpg",
                              # 'atlas://data/images/defaulttheme/button_disabled_pressed'
                              # /usr/lib/python3/dist-packages/kivy/data/images/defaulttheme-0.png
                              # /usr/lib/python3/dist-packages/kivy/data/images/defaulttheme.atlas
                              #imagesource="/home/dalem/PycharmProjects/soundBoard/pearl.jpg"

                              # Doesn't work... Might be because it's included in another widget?
                              #on_press=lambda a: self.callback(self),
                              )
        self.add_widget(button2)

        print("MyApp.build Label")
        self.add_widget(Label(text='Hello world label'))
        self.add_widget(Label(text='next Hello world label'))
        self.add_widget(Label(text='3rd Hello world label'))
        print("build done")


class MyApp(App):

    def build(self):
        return aScreen()

if __name__ == '__main__':
    print("Main code in python main.py script.")
    MyApp().run()
