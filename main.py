from kivy.base import runTouchApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from kivy.uix.widget import Widget

from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.graphics import Rotate

import math

Window.size = (640, 480)
Window.set_title('My Space Game')
Window.set_system_cursor(cursor_name='crosshair')


Builder.load_string('''
<Root>:
    Earth:
        pos: root.width / 2 - self.width / 2, root.height / 2 - self.height / 2
        size: self.size
    Moon:
        pos: root.width / 2 - self.width / 2, root.height / 2 - self.height / 2
        size: root.width / 16, root.width / 16

<Earth>
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Ellipse:
            # Earth
            size: self.size
            pos: self.pos
            source: 'pexels-pixabay-87651-earth.png'
<Moon>
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Ellipse:
            # Moon
            id: moon
            size: self.size
            pos: self.pos
            source: 'pexels-alex-andrews-821718-moon.png'
    Label:
        id: moon_label
        text: self.text
    Label:
        id: score
        text: self.text
''')

class Root(Widget):
    pass

class Earth(Widget):
    pass

class Moon(Widget):
    angle = 0
    distance = 200
    text = ""
    score = 0

    def __init__(self, **kwargs):
        super(Moon, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/80.)
        

    def update(self, *args):
        self.angle += 1
        self.x = (Window.width - self.width)/2 + self.distance*math.cos(self.angle/360*math.pi)
        self.y = (Window.height - self.height)/2 + self.distance*math.sin(self.angle/360*math.pi)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print('hit')
            self.score += 1
            self.ids.moon_label.text = "Hit! Score : " + str(self.score)

if __name__ == '__main__':
    runTouchApp(Root())