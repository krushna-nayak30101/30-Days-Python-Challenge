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
