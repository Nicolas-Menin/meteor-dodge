import arcade
from config import HEIGHT, SPEED




class Background(arcade.Sprite):

    def __init__(self,x):
        super().__init__("app/assets/EspacioLargo.png")
        self.center_x = x
        self.center_y = HEIGHT / 2
        self.width_bg = self.width



    def update(self,delta_time, *args, **kwargs):


        self.center_x -= SPEED

        if self.right < 0:
            self.center_x += self.width_bg * 2
