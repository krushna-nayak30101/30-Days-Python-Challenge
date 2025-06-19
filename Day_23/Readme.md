# 🎯 Topic: 
- 🔹 How to parse command-line arguments using argparse
- 🔹 Structuring user-friendly CLI tools
- 🔹 Handling options, flags, and help messages

Challennge -   Rebuild the Temperature Converter from Day 22 using Kivy GUI, with:
Text input field
Spinner for unit selection
Button to trigger conversion

```
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
```

```
<TempConverter>:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    Label:
        text: "Temperature Converter"
        font_size: 24
        size_hint_y: None
        height: 40

    TextInput:
        id: temp_input
        hint_text: "Enter temperature"
        multiline: False
        input_filter: 'float'

    Spinner:
        id: unit_spinner
        text: "Celsius"
        values: ["Celsius", "Fahrenheit"]
        size_hint_y: None
        height: 44

    Button:
        text: "Convert"
        on_press: root.convert()

    Label:
        text: root.result
        font_size: 18
        color: (1, 1, 1, 1)
```

🔑 Key Learning:

Kivy introduces event-driven programming in a visually interactive way.
 It’s perfect for modern retail tools, dashboards, kiosk interfaces, and mobile apps.
 


