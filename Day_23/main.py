from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class TempConverter(BoxLayout):
    result = StringProperty("")

    def convert(self):
        try:
            temp = float(self.ids.temp_input.text)
            unit = self.ids.unit_spinner.text.lower()
            if unit == "celsius":
                converted = (temp - 32) * 5 / 9
                self.result = f"{temp}°F is {converted:.2f}°C"
            else:
                converted = (temp * 9 / 5) + 32
                self.result = f"{temp}°C is {converted:.2f}°F"
        except:
            self.result = "❌ Enter a valid number."

class TempApp(App):
    def build(self):
        return TempConverter()

if __name__ == '__main__':
    TempApp().run()
