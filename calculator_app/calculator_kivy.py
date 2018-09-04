# calculator_kivy.py
# The python script which will display the calculator operation.
#
# Execution:-- python calculator-kivy.py
#
# Author:- Koshti Nikhilesh


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
__version__ = "1.0"

class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = str("ERROR")


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()


calculator = CalculatorApp()
calculator.run()
