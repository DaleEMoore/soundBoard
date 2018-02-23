#!/usr/bin/env python2
# TODO; minimize this so it's easier to change/test
# button1 couldn't go to GridView... really messed up!

# From: https://stackoverflow.com/questions/17392202/passing-image-object-as-a-button-background-in-kivy

# TODO; add sound volume control.
# TODO; add sound pause and play control.
# TODO; tie the image closer to the sound_file in the source code. Right now they are very distant.
# TODO; on selecting an image/sound_file screen size display the image and display the sound controls.


print("The start of everything.")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
import sys
import time

# Worked
# friday.png
# fossilMuseum.png
# TeslaBottle.png
# source: 'daleemoore.mooreworks.org/JoulesSB/BabyHefridayartbeat.png'

# Worked
# source: 'kivy-logo-black-64.png'
# From: https://kivy.org/logos/kivy-logo-black-64.png

# TODO; setup another button with a different picture and sound.
# TODO; make space in columns and rows for buttons and images
#       GridLayout:
#           columns: 3
built = Builder.load_string("""
<ButtonsApp>:
    orientation: "vertical"
    Button:
        text: "B1"
        id: B1
        on_press: root.callback(self, "B1")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/friday.png'        
            #source: 'kivy.png'
            y: self.parent.y + self.parent.height - 255
            x: self.parent.x
            size: dp(250), dp(250)
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Label:
        text: "A label"
    Label:
        text: "B label"
    Label:
        text: "C label"
    Label:
        text: "D label"
    Label:
        text: "E label"
    Label:
        text: "F label"
    Label:
        text: "G label"
    Label:
        text: "H label"
    Button:
        text: "B2"
        id: B2
        on_press: root.callback(self, "B2")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/BabySister.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Label:
        text: "A label"
    Label:
        text: "B label"
    Label:
        text: "C label"
    Label:
        text: "D label"
    Label:
        text: "E label"
    Label:
        text: "F label"
    Label:
        text: "G label"
    Label:
        text: "H label"
    Button:
        text: "B3"
        id: B3
        on_press: root.callback(self, "B3")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/buzzlightyearinfinitybeyond.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Button:
        text: "B4"
        id: B4
        on_press: root.callback(self, "B4")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/BabyHeartbeat.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Button:
        text: "B5"
        id: B5
        on_press: root.callback(self, "B5")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/fossilMuseum.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Button:
        text: "B6"
        id: B6
        on_press: root.callback(self, "B6")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/helicopter.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Button:
        text: "B7"
        id: B7
        on_press: root.callback(self, "B7")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/JoulesLaugh.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Button:
        text: "B8"
        id: B8
        on_press: root.callback(self, "B8")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/mytubeGood.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Button:
        text: "B9"
        id: B9
        on_press: root.callback(self, "B9")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/Share.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Button:
        text: "B10"
        id: B10
        on_press: root.callback(self, "B10")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/TeslaBottle.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Button:
        text: "B11"
        id: B11
        on_press: root.callback(self, "B11")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/TeslaForggie2.png'        
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
""")

class ButtonsApp(App, BoxLayout):
    def callback(self, instance, value):
        #print("Button pushed instance")
        print('The button %s instance.' % str(instance.text))
        #print("value")
        print('The button %s value.' % str(value))
        #print('The button <%s> is being pressed' % instance.text)
        print ('start sound')
        if value == "B1":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/friday.mp3')
        if value == "B2":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/BabySister.mp3')
        if value == "B3":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/buzzlightyearinfinitybeyond.mp3')
        if value == "B4":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/BabyHeartbeat.mp3')
        if value == "B5":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/fossilMuseum.mp3')
        if value == "B6":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/helicopter.mp3')
        if value == "B7":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/JoulesLaugh.mp3')
        if value == "B8":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/mytubeGood.mp3')
        if value == "B9":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/Share.mp3')
        if value == "B10":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/TeslaBottle.mp3')
        if value == "B11":
            sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/TeslaFroggie2.mp3')
            #sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/BabyHeartbeat.mp3')
        if sound:
            print("Sound found at %s" % sound.source)        #print("Button " + str(self.ids["B20"].text))

            print("Sound is %.3f seconds" % sound.length)
            try:
                sound.play()
                print('start waiting for sound to finish')
                # TODO; change button appearance to depressed, maybe just .text = name.
                # wait until the sound is done playing to free up the interface
                # Well it doesn't really freeze, you can push the same button and buffer up several plays.
                time.sleep(sound.length)
                print('sound done.')
                # TODO; change button appearance to pix.
            except:
                print("I couldn't play the sound assiciated with %s because %s" % (str(value), sys.exc_info()[0]))
        else:
            print("No sound.")
        #sound = SoundLoader.load('beep.wav')
        #AttributeError: 'NoneType' object has no attribute 'play'
        #sound.play()


    def on_press(self):
        print ('%s pressed' % str(self))

    def build(self):
        print("ButtonsApp.build()")
        print("Button " + str(self.ids["B1"].text))

        # TODO; B20 and B30 don't press?
        self.add_widget(Button(text="B20",id="B20"))
        self.bind(on_press=lambda a: self.callback(self, "B20"))
        # TODO; add_widget did not put B20 in ids.
        # KeyError: 'B20'
        #self.add_widget(Button(text="B30",id="B30"))
        #self.bind(on_press=lambda a: self.callback(self, "B30"))
        return self


if __name__ == "__main__":
    print ("built: " + str(built))
    root_widget = ButtonsApp().run()
    print ("root_widget: " + str(root_widget))
