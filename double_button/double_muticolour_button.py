from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

class ScatterWidget(BoxLayout):
    def change_color(self):
       color = [random.random() for i in xrange(3)] + [1]
       label = self.ids["my_label"]
       label.color=color

class mainclass1(App):
    def build(self):
        return ScatterWidget()




mainclass1().run()
