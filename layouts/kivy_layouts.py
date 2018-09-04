# kivy_layouts.py
#
# The kivy-python script which contains 
# different kivy layouts.
# Author:-- Koshti Nikhilesh



from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.slider import Slider

class CustomPopup(Popup):
    pass


class SampleBoxLayout(BoxLayout):
    checkbox_is_Active = ObjectProperty(False)
    
    def check_status(self, value):
        if value is True:
            print " checkbox checked "
        else:
            print " CHeckbox unchecked "
    
    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)


    def OnSliderValueChange(self,instance,value):
        print "#################", value



    def switch_on(self, instance, value):
        print value
        if value is True:
            print " switch on "
        else:
            print "switch off "        

    def open_popup():
        the_popup = CustomPopup()
        the_popup.open()

    def spinner_clicked(self, instance, value):
        print "######################", value




class SampleApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return SampleBoxLayout()



c = SampleApp()
c.run()        
