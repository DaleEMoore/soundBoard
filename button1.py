#!/usr/bin/env python2
# From: https://stackoverflow.com/questions/17392202/passing-image-object-as-a-button-background-in-kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ButtonsApp>:
    orientation: "vertical"
    Button:
        text: "B1"
        id: B1
        on_press: root.callback()
        Image:
            # From: https://kivy.org/logos/kivy-logo-black-64.png
            source: 'kivy-logo-black-64.png'        
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
    def build(self):

        return self

    def callback(instance):
        print('The button is being pressed.')
        #print('The button <%s> is being pressed' % instance.text)


if __name__ == "__main__":
    ButtonsApp().run()