import arcade



class Button(arcade.Sprite):

    def __init__(self,idle,hover,x,y,action,load_sound):
        super().__init__(idle)
        self.center_x = x
        self.center_y = y
        self.img_idle = arcade.load_texture(idle)
        self.img_hover = arcade.load_texture(hover)
        self.action = action
        self.hovered = False
        self.load_sound = load_sound
        self.play_sound = None

