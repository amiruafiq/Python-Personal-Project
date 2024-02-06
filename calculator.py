from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CalculatorApp(App):
    def build(self):
        self.operators = ['/', '*', '-', '+']
        self.last_was_operator = None
        self.last_button = None

        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Entry widget for displaying the input and result
        self.entry = TextInput(font_size=32, multiline=False, readonly=True, halign='right', input_filter='float')
        layout.add_widget(self.entry)

        # Grid layout for buttons
        buttons_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.8))

        # Buttons for numbers and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for button_text in buttons:
            btn = Button(text=button_text, font_size=32)
            btn.bind(on_press=self.on_button_click)
            buttons_layout.add_widget(btn)

        layout.add_widget(buttons_layout)

        return layout

    def on_button_click(self, instance):
        current_text = self.entry.text
        button_text = instance.text

        if button_text == '=':
            try:
                result = eval(current_text)
                self.entry.text = str(result)
            except Exception as e:
                self.entry.text = "Salah tu Boh"
        else:
            if self.last_was_operator and button_text in self.operators:
                # Replace the last operator if the new one is pressed
                self.entry.text = current_text[:-1] + button_text
            else:
                # Append the clicked button to the input
                self.entry.text += button_text

        self.last_button = button_text
        self.last_was_operator = button_text in self.operators

if __name__ == '__main__':
    CalculatorApp().run()
