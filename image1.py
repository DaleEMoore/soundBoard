#!/usr/bin/env python2
# TODO; run throught the example kivy and see if there's images in buttons or labels.
# Let's get kivy to display the image files sized well and centered.
print("The start of everything.")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
import time
# This gets added on to the root widget.
# TODO; what is the root widget?
built1 = Builder.load_string("""
<ButtonsApp>:
    #orientation: "vertical"
    Button:
        text: "B1"
        id: B1
        on_press: root.callback(self, "B1")
        size_hint_x: None
        size_hint_y: None
        width: 100
        #size: 250, 250
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/friday.png'        
            ##source: 'kivy.png'
            y: self.parent.y + self.parent.height - 120
            x: self.parent.x
            #y: self.parent.y + self.parent.height - 250
            #x: self.parent.x
            #size: 250, 250
            #allow_stretch: True
            #center_x: self.parent.center_x
            #center_y: self.parent.center_y            
    Button:
        text: "B2"
        id: B2
        on_press: root.callback(self, "B2")
        size_hint_x: None
        size_hint_y: None
        #size: 250, 250
        width: 100
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/BabySister.png'        
            y: self.parent.y + self.parent.height - 120
            x: self.parent.x
            #size: 250, 250
            #allow_stretch: True
            #center_x: self.parent.center_x
            #center_y: self.parent.center_y            
""")
# This just gets added on to the root widget.
built2 = Builder.load_string("""
<ButtonsApp>:
    #orientation: "vertical"
    Button:
        text: "B1"
        id: B1
        on_press: root.callback(self, "B1")
        size_hint_x: None
        size_hint_y: None
        width: 100
        #size: 250, 250
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/friday.png'        
            ##source: 'kivy.png'
            y: self.parent.y + self.parent.height - 120
            x: self.parent.x
            #y: self.parent.y + self.parent.height - 250
            #x: self.parent.x
            #size: 250, 250
            #allow_stretch: True
            #center_x: self.parent.center_x
            #center_y: self.parent.center_y            
    Button:
        text: "B2"
        id: B2
        on_press: root.callback(self, "B2")
        size_hint_x: None
        size_hint_y: None
        #size: 250, 250
        width: 100
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/BabySister.png'        
            y: self.parent.y + self.parent.height - 120
            x: self.parent.x
            #size: 250, 250
            #allow_stretch: True
            #center_x: self.parent.center_x
            #center_y: self.parent.center_y            
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
                print("I couldn't play the sound assiciated with %s" % str(value))
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

        ## TODO; B20 and B30 don't press?
        #self.add_widget(Button(text="B20",id="B20"))
        #self.bind(on_press=lambda a: self.callback(self, "B20"))
        ## TODO; add_widget did not put B20 in ids.
        # KeyError: 'B20'
        #self.add_widget(Button(text="B30",id="B30"))
        #self.bind(on_press=lambda a: self.callback(self, "B30"))
        return self


if __name__ == "__main__":
    print ("built1: " + str(built1))
    root_widget = ButtonsApp().run()
    print ("root_widget: " + str(root_widget))
