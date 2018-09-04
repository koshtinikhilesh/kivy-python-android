# sample_button.py
# The python script for displaying the single button.
#
# Author:- Koshti Nikhilesh


from kivy.app import App
from kivy.uix.button import Button




class mainclass(App):
    def build(self):
        return Button(text='HELLO')




mainclass().run()
