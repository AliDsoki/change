from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from random import randint

class RootWidget(BoxLayout):
    def change_background(self):
        self.canvas.before.clear()
        with self.canvas.before:
            r, g, b = [randint(0, 255) / 255.0 for _ in range(3)]
            Color(r, g, b, 1)
            Rectangle(pos=self.pos, size=self.size)

class ChangeColorApp(App):
    def build(self):
        return RootWidget()