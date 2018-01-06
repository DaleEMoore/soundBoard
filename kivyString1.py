#!/usr/bin/env python2
# From: https://stackoverflow.com/questions/17392202/passing-image-object-as-a-button-background-in-kivy
print("The start of everything.")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button

# Worked
# friday.png
# fossilMuseum.png
# TeslaBottle.png
# source: 'daleemoore.mooreworks.org/JoulesSB/BabyHeartbeat.png'

# Worked
# source: 'kivy-logo-black-64.png'
# From: https://kivy.org/logos/kivy-logo-black-64.png

toBuild = """
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
    Button:
        text: "B2"
        id: B2
        on_press: root.callback(self, "B2")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/BabySister.png'        
            #source: 'kivy.png'
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
    Button:
        text: "B3"
        id: B3
        on_press: root.callback(self, "B3")
        Image:
            source: 'daleemoore.mooreworks.org/JoulesSB/buzzlightyearinfinitybeyond.png'        
            #source: 'kivy.png'
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
            center_x: self.parent.center_x
            center_y: self.parent.center_y            
"""
#built = Builder.load_string("""

class ButtonsApp(App, BoxLayout):
    def callback(self, instance, value):
        #print("Button pushed instance")
        print('The button %s instance.' % str(instance.text))
        #print("value")
        print('The button %s value.' % str(value))
        #print('The button <%s> is being pressed' % instance.text)

    def on_press(self):
        print ('%s pressed' % str(self))
        pass

    def build(self):
        print("ButtonsApp.build()")
        print("Button " + str(self.ids["B1"].text))

        # TODO; cB2 and cB3 don't press?
        # TODO; how do I set the 'id=' value to the name of the widget?
        # Here is some help
        # https://stackoverflow.com/questions/45171309/how-to-get-id-and-text-value-of-a-kivy-button-as-string
        # Though the example has buttons with ids of "text" and labels with ids of reference. Where reference is
        # not a string.
        self.add_widget(Button(text="cB2",id="cB2"))
        self.bind(on_press=lambda a: self.callback(self, "cB2"))
        # TODO; add_widget did not put B2 in ids.
        # KeyError: 'B2'
        #print("Button " + str(self.ids["B2"].text))
        self.add_widget(Button(text="cB3",id="cB3"))
        self.bind(on_press=lambda a: self.callback(self, "cB3"))
        #print("Button " + str(self.ids["B3"].text))
        return self


if __name__ == "__main__":
    print("Starting...")
    built = Builder.load_string(toBuild)
    print ("built: " + str(built))
    root_widget = ButtonsApp().run()
    print ("root_widget: " + str(root_widget))
