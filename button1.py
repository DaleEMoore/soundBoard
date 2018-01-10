#!/usr/bin/env python2
# From: https://stackoverflow.com/questions/17392202/passing-image-object-as-a-button-background-in-kivy
print("The start of everything.")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
import time

# Worked
# friday.png
# fossilMuseum.png
# TeslaBottle.png
# source: 'daleemoore.mooreworks.org/JoulesSB/BabyHeartbeat.png'

# Worked
# source: 'kivy-logo-black-64.png'
# From: https://kivy.org/logos/kivy-logo-black-64.png

# TODO; setup another button with a different picture and sound.
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
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Label:
        text: "A label"
""")

class ButtonsApp(App, BoxLayout):
    def callback(self, instance, value):
        #print("Button pushed instance")
        print('The button %s instance.' % str(instance.text))
        #print("value")
        print('The button %s value.' % str(value))
        #print('The button <%s> is being pressed' % instance.text)
        print ('start sound')
        sound = SoundLoader.load('daleemoore.mooreworks.org/JoulesSB/friday.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
            # wait until the sound is done playing to free up the interface
            # Well it doesn't really freeze, you can push the same button and buffer up several plays.
            print('start waiting for sound to finish')
            time.sleep(sound.length)
            print ('sound done.')
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

        # TODO; B2 and B3 don't press?
        self.add_widget(Button(text="B2",id="B2"))
        self.bind(on_press=lambda a: self.callback(self, "B2"))
        # TODO; add_widget did not put B2 in ids.
        # KeyError: 'B2'
        #print("Button " + str(self.ids["B2"].text))
        self.add_widget(Button(text="B3",id="B3"))
        self.bind(on_press=lambda a: self.callback(self, "B3"))
        #print("Button " + str(self.ids["B3"].text))
        return self


if __name__ == "__main__":
    print ("built: " + str(built))
    root_widget = ButtonsApp().run()
    print ("root_widget: " + str(root_widget))
