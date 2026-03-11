import arcade
from entities.background import Background
from ui.buttons import Button
from ui.images import Images

class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.bg_list = None
        self.menu_elements = None
        self.buttons_elements = None
        self.buttons = None
        self.bg = None
        self.bg2 = None
        self.title_game = None
        self.btn_start =None
        self.btn_configuration = None
        self.quit_button = None


    def setup(self):
        self.bg_list = arcade.SpriteList()
        self.menu_elements =arcade.SpriteList()
        self.buttons_elements = arcade.SpriteList()
        self.bg = Background(750)
        self.bg2 = Background(2250)
        self.title_game = Images("app/assets/Title.png",250,400)
        self.buttons = [Button("app/assets/Start_idle.png",
                               "app/assets/Start_hover.png",250,200,
                               self.window.game_view,self.window.button_sound),
                        Button("app/assets/Configuracion_idle.png",
                               "app/assets/Configuracion_hover.png",250,150,
                               self.window.configuration_view,self.window.button_sound)]


        self.quit_button = Button("app/assets/Quit_idle.png",
                               "app/assets/Quit_hover.png",250,100,
                               arcade.close_window,self.window.button_sound)

        self.buttons_elements.extend(self.buttons)
        self.buttons_elements.append(self.quit_button)
        self.menu_elements.append(self.title_game)
        self.bg_list.append(self.bg)
        self.bg_list.append(self.bg2)


    def on_update(self, delta_time):


        self.bg_list.update(delta_time)
        self.menu_elements.update(delta_time)
        self.buttons_elements.update(delta_time)

    def on_draw(self):


        self.bg_list.draw()
        self.menu_elements.draw()
        self.buttons_elements.draw()


    def on_mouse_press(self, x, y, button, modifiers):


        for button in self.buttons_elements:
            if button.hovered:
                button.play_sound = arcade.play_sound(button.load_sound,self.window.sound_volume)
                if self.quit_button.collides_with_point((x,y)):
                    self.quit_button.action()
                else:

                    button.action.setup()
                    self.window.show_view(button.action)

    def on_mouse_motion(self, x, y, dx, dy):

        for button in self.buttons_elements:
            if button.collides_with_point((x,y)):
                if not button.hovered:
                    button.play_sound = arcade.play_sound(button.load_sound,self.window.sound_volume)
                    button.hovered = True
                button.texture = button.img_hover

            else:

                button.texture = button.img_idle
                button.hovered = False

