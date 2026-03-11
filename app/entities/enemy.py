import random
import arcade
from config import WIDTH



class Enemy(arcade.Sprite):

    def __init__(self,filename):
        super().__init__(filename)

        self.center_x = -40
        self.center_y = random.randint(50,900)
        self.enemy_speed = random.randint(5,10)


    def update(self,delta_time, *args, **kwargs):



        self.center_x += self.enemy_speed
        self.center_y -= self.enemy_speed

        if self.left > WIDTH :
            self.center_x = -40
            self.enemy_speed = random.randint(5,10)
            self.center_y = random.randint(50,900)


