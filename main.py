from kivy.base import runTouchApp
from kivy.lang import Builder

from kivy.uix.widget import Widget

from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.core.window import Window

from random import random
import math

Window.size = (640, 480)

Builder.load_string('''
<Root>:
    Earth:
        pos: root.width / 2 - self.width / 2, root.height / 2 - self.height / 2
    Moon:
        pos: root.width / 2 - self.width / 2, root.height / 2 - self.height / 2
<Earth>
    canvas:
        Color:
            rgba: 1, 0, 0, 1
        # Rectangle:
        #     pos: self.pos
        #     size: self.size
        Ellipse:
            # Earth
            size: self.size
            pos: self.pos
            source: 'pexels-pixabay-87651-earth.png'
<Moon>
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        # Rectangle:
        #     pos: self.pos
        #     size: self.size
        Ellipse:
            # Moon
            size: self.size
            pos: self.pos
            source: 'pexels-alex-andrews-821718-moon.png'
''')

class Root(Widget):
    pass

class Earth(Widget):
    pass

class Grid(Widget):
    pass

class Moon(Widget):
    # location = ListProperty([300,300])
    angle = 0

    def __init__(self, **kwargs):
        super(Moon, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60.)

    def update(self, *args):
        Animation.cancel_all(self)
        self.angle += 10
        # self.x += math.sin(self.angle/360*math.pi)
        # self.y += math.cos(self.angle/360*math.pi)
        self.x = (Window.width/2 - self.width/2) + 100*math.cos(self.angle/360*math.pi)
        self.y = (Window.height/2 - self.height/2) + 100*math.sin(self.angle/360*math.pi)

    
    # def anim_to_random_pos(self):
    #     Animation.cancel_all(self)
    #     random_x = math.sin() * (Window.width - self.width)
    #     random_y = math.cos() * (Window.height - self.height)

    #     anim = Animation(x=random_x, y=random_y,
    #         duration = 4,
    #         t = 'out_elastic')
    #     anim.start(self)
        
    # def on_touch_down(self, touch):
    #     if self.collide_point(*touch.pos):
    #         self.anim_to_random_pos()


if __name__ == '__main__':
    runTouchApp(Root())