import arcade





class Images(arcade.Sprite):

    def __init__(self,image,x,y):
        super().__init__(image)

        self.center_x = x
        self.center_y = y
