import arcade
from config import HEIGHT



class Player(arcade.Sprite):

    def __init__(self,warble_sound):
        super().__init__("app/assets/UFO.png")
        self.center_x = 250
        self.center_y = 250
        self.change_x = 0
        self.center_y = 0
        self.moving = None
        self.warble_sound_load = warble_sound
        self.warble_sound_play = None



    def update(self, delta_time, *args, **kwargs):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > HEIGHT:
            self.right = HEIGHT - 2

        if self.top > HEIGHT:
            self.top = HEIGHT - 2

        elif self.bottom < 0:
            self.bottom = 0
