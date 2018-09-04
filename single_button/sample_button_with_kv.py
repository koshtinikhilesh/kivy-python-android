from kivy.app import App
from kivy.uix.button import Button


class ScatterWidget(Button):
    pass

class mainclass(App):
    def build(self):
        return ScatterWidget()




mainclass().run()
