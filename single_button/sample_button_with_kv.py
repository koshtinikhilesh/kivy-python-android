# sample_button_with_kv.py
# The python script with the kiv file format for 
# displaying the single button
#
#
# Author:-- Koshti Nikhilesh




from kivy.app import App
from kivy.uix.button import Button


class ScatterWidget(Button):
    pass

class mainclass(App):
    def build(self):
        return ScatterWidget()




mainclass().run()
