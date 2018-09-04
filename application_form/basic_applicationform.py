# basic_applicationform.py
#
# The python script for displaying the basic application form.
#
# Author:- Koshti Nikhilesh



from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput




class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        # LoginScreen class, which will inherit from GridLayout. We use super to avoid needing to refer to the base class, as well as utilize multi-inheritance.
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username:"))
        self.username = TextInput()
        self.add_widget(self.username)
        self.add_widget(Label(text="Password:"))
        self.password = TextInput(password=True)
        self.add_widget(self.password)
        self.add_widget(Label(text="Two Factor Auth:"))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)



class SimpleKivy(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    SimpleKivy().run()
