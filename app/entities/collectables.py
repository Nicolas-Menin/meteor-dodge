import arcade
import random
from config import HEIGHT,WIDTH

class Collectable(arcade.Sprite):

    def __init__(self,image,time_spawn,speed_minimum,speed_limit):
        super().__init__(image)

        self.time_spawn = time_spawn
        self.speed_minimum = speed_minimum
        self.speed_limit = speed_limit
        self.timer = 0
        self.picked = False

        self.spawn()

    def update(self, delta_time, *args, **kwargs):



        if self.timer < self.time_spawn:
            self.timer += delta_time

        else:
            self.center_x -= self.speed
            if self.right < 0:
                self.spawn()
                self.timer = 0


    def spawn(self):

        self.speed = random.randint(self.speed_minimum,self.speed_limit)
        self.center_x = WIDTH*2
        self.center_y = random.randint(0,HEIGHT)
