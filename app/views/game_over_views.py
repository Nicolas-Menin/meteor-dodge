import arcade
from ui.buttons import Button
from ui.images import Images
from entities.background import Background


class GameOverView(arcade.View):

    def __init__(self):
        super().__init__()

        self.bg_list = None
        self.bg = None
        self.bg2 = None
        self.game_over_images = None
        self.game_over_buttons = None
        self.yes_button = None
        self.no_button = None
        self.game_over_image = None
        self.retry_image = None
        arcade.stop_sound(self.window.music_bg)
        self.game_over_sound = None

    def setup(self):

        self.game_over_sound = arcade.play_sound(self.window.game_over_sound,
                                                 self.window.sound_volume)
        self.bg_list = arcade.SpriteList()
        self.game_over_images = arcade.SpriteList()
        self.game_over_buttons = arcade.SpriteList()

        self.bg = Background(750)
        self.bg2 = Background(2250)

        self.yes_button = Button("app/assets/Si_idle.png",
                                 "app/assets/Si_hover.png",350,235,self.window.game_view,
                                 self.window.button_sound)
        self.no_button = Button("app/assets/No_idle.png",
                                 "app/assets/No_hover.png",150,235,self.window.main_menu_view,
                                 self.window.button_sound)
        self.game_over_image = Images("app/assets/GameOver.png",250,400)
        self.retry_image = Images("app/assets/Retry.png",250,320)

        self.game_over_images.append(self.game_over_image)
        self.game_over_images.append(self.retry_image)

        self.game_over_buttons.append(self.yes_button)
        self.game_over_buttons.append(self.no_button)

        self.bg_list.append(self.bg)
        self.bg_list.append(self.bg2)

    def on_mouse_press(self, x, y, button, modifiers):


        for button in self.game_over_buttons:
            if button.collides_with_point((x,y)):
                button.play_sound = arcade.play_sound(button.load_sound,self.window.sound_volume)
                button.action.setup()
                self.window.music_bg.play()
                self.window.show_view(button.action)

    def on_mouse_motion(self, x, y, dx, dy):

        for button in self.game_over_buttons:
            if button.collides_with_point((x,y)):
                if not button.hovered:
                    button.play_sound = arcade.play_sound(button.load_sound,
                                                          self.window.sound_volume)
                    button.hovered = True
                button.texture = button.img_hover

            else:
                button.texture = button.img_idle
                button.hovered = False


    def on_update(self, delta_time):

        self.bg_list.update(delta_time)
    def on_draw(self):

        self.bg_list.draw()
        self.game_over_images.draw()
        self.game_over_buttons.draw()