# increment_Decrement_number.py
# The script for incrementing and decrementing the number using kivy button
#
#
# it will create a black windows using rows=1 in griglayout



from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty


Builder.load_file('kv/buttons.kv')

class AddButton(Button):
    pass

class SubtractButton(Button):
    pass
class container(GridLayout):

    def add_one(self):
        value = int(self.display.text)
        self.display.text = str(value + 1)


    def subtract_one(self):

        value = int(self.display.text)
        self.display.text = str(value - 1)

class BasicKivyApp(App):
    def build(self):
        self.title = "Awesome App"
        return container()


if __name__ == '__main__':
    BasicKivyApp().run()
