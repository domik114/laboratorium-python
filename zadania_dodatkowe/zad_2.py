from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from matplotlib import pyplot as plt

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        inLayout = GridLayout(rows=3, size_hint=(0.3, 1))

        inLayout.add_widget(Button(text='Function 1'))
        inLayout.add_widget(Button(text='Function 2'))
        inLayout.add_widget(Button(text='Function 3'))

        layout.add_widget(inLayout)
        layout.add_widget(Button(text='Chart pane'))

        return layout


if __name__ == '__main__':
    MyApp().run()