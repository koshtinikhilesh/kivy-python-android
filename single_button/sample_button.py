from kivy.app import App
from kivy.uix.button import Button




class mainclass(App):
    def build(self):
        return Button(text='HELLO')




mainclass().run()
