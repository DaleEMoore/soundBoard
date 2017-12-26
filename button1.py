#!/usr/bin/env python2
# From: https://stackoverflow.com/questions/17392202/passing-image-object-as-a-button-background-in-kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button

built = Builder.load_string("""
<ButtonsApp>:
    orientation: "vertical"
    Button:
        text: "B1"
        id: B1
        on_press: root.callback(self)
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
    def callback(self, instance):
        print('The button is being pressed.')
        #print('The button <%s> is being pressed' % instance.text)

    def build(self):
        print("ButtonsApp.build()")
        print("Button " + str(self.ids["B1"].text))
        self.add_widget(Button(text="B2",id="B2"))
        self.bind(on_press=lambda a: self.callback(self))
        # TODO; add_widget did not put B2 in ids.
        # KeyError: 'B2'
        #print("Button " + str(self.ids["B2"].text))
        return self



if __name__ == "__main__":
    print ("built: " + str(built))
    root_widget = ButtonsApp().run()
    print ("root_widget: " + str(root_widget))
