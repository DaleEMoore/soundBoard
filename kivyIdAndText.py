# From: https://stackoverflow.com/questions/45171309/how-to-get-id-and-text-value-of-a-kivy-button-as-string
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

import sys
# Notice that "id:" can have strings bounded by double-quotes like '"Btn1"' or without the double-quotes like 'lobj'.

kv_file = '''
<MyButton@Button>:
    color: .8,.9,0,1
    font_size: 25

<KVMyHBoxLayout>:
    orientation: 'vertical'
    MyButton:
        id:'idBtn1'
        text: 'Btn1'
        background_color: 1,0,0,1
        on_press:app.Pressbtn(self)
    MyButton:
        id:"idBtn2"
        text: "Btn2"
        background_color: 0,1,0,1
        on_press:app.Pressbtn(self)
    MyButton:
        id: lobj
        text: "Object"
        background_color: 1,0,1,1
        on_press:app.Pressbtn(self)
    MyButton:
        id: lid
        text: "ID"
        background_color: 0,0,1,1
        on_press:app.Pressbtn(self)
    MyButton:
        id: ltext
        text: "Text"
        background_color: 1,0,1,1
        on_press:app.Pressbtn(self)
    MyButton:
        id: lcomment
        text: "Comment"
        background_color: 1,0,1,1
        on_press:app.Pressbtn(self)       
'''


class KVMyHBoxLayout(BoxLayout):
    pass

class ExampleApp(App):
    def Pressbtn(self, instance):
        # add some type of description before the value.
        instance.parent.ids.lobj.text = "Object:" + str(instance)
        instance.parent.ids.lid.text= "ID:" + self.get_id(instance)
        instance.parent.ids.ltext.text = "Text:" + instance.text
        try:
            # TODO; getting TypeError in "instance.parent.ids(self.get_id(instance)".
            inst3 = self.get_id(instance)
            inst4 = instance.parent.ids[inst3]
            instance.parent.ids.lcomment.text = "Comment: id contains:" + inst4
        except:
            instance.parent.ids.lcomment.text = "Comment: error " + str(sys.exc_info()[0])
    def get_id(self,  instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id

    def build(self):
        Builder.load_string(kv_file)
        return KVMyHBoxLayout()

if __name__ == "__main__":
    app = ExampleApp()
    app.run()