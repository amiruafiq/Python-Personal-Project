from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # Create a box layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=(10, 10))

        # Create a label
        self.label = Label(text="Welcome to Kivy GUI", font_size=20)

        # Create a button
        button = Button(text="Click Me", on_press=self.on_button_click, size_hint=(None, None))
        button.size = (200, 50)

        # Add widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        self.label.text = "Button Clicked!"
        instance.text = "Clicked!"

if __name__ == '__main__':
    MyApp().run()
