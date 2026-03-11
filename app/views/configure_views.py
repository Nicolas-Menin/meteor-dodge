import arcade
from ui.images import Images
from entities.background import Background
from ui.buttons import Button

class ConfigurationView(arcade.View):
    def __init__(self):
        super().__init__()

        # Fodno
        self.bg = None
        self.bg2 = None
        # Barras y Sprites
        self.rect = None
        self.music_bar = None
        self.sound_bar = None
        self.music_icon = None
        self.sound_icon = None
        self.img_music = None
        self.img_volume = None

        # Listas de elementos
        self.bg_list = None
        self.config_lst = None

        # Variables de control
        self.drag_music = False
        self.drag_sound = False
        self.music_volume = None
        self.sound_volume = None
        self.windows = None
        self.music_load = None

        # Boton

        self.back = None

    def setup(self):
        self.config_lst = arcade.SpriteList()
        self.bg_list = arcade.SpriteList()
        # Barras de volumen
        self.music_bar = arcade.Rect(170, 330, 100, 100, 150, 20, 250, 350)
        self.sound_bar = arcade.Rect(170, 330, 100, 100, 150, 20, 250, 200)

        # Fondo
        self.bg = Background(750)
        self.bg2 = Background(2250)

        # Iconos
        self.music_icon = arcade.SpriteCircle(15, arcade.color.WHITE)
        self.music_icon.center_x = self.window.music_bar
        self.music_icon.center_y = 350

        self.sound_icon = arcade.SpriteCircle(15, arcade.color.WHITE)
        self.sound_icon.center_x = self.window.sound_bar
        self.sound_icon.center_y = 200

        # Imágenes
        self.img_music = Images("app/assets/Musica.png", 250, 400)
        self.img_volume = Images("app/assets/Sonido.png", 250, 250)

        # Boton

        self.back = Button("app/assets/Back_idle.png",
                           "app/assets/Back_hover.png",
                           70,50,self.window.main_menu_view,
                           self.window.button_sound)

        # Agregar a la lista de sprites
        self.config_lst.append(self.music_icon)
        self.config_lst.append(self.sound_icon)
        self.config_lst.append(self.img_music)
        self.config_lst.append(self.img_volume)
        self.bg_list.append(self.bg)
        self.bg_list.append(self.bg2)
        self.bg_list.append(self.back)

        # Volumen inicial
        self.music_volume = (self.music_icon.center_x - 170) / (330 - 170)
        self.sound_volume = (self.sound_icon.center_x - 170) / (330 - 170)

    def on_update(self, delta_time):

        self.bg_list.update()

    def on_draw(self):
        self.clear()
        self.bg_list.draw()

        arcade.draw_rect_filled(self.music_bar, (28, 44, 77))
        arcade.draw_rect_filled(self.sound_bar, (28, 44, 77))

        # Dibujar sprites
        self.config_lst.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.sound_icon.collides_with_point((x, y)):
            self.drag_sound = True

        if self.music_icon.collides_with_point((x, y)):
            self.drag_music = True

        if self.back.collides_with_point((x,y)):
            if self.back.hovered:
                self.back.play_sound = arcade.play_sound(self.back.load_sound,self.window.sound_volume)
                self.back.action.setup()
                self.window.show_view(self.back.action)

    def on_mouse_motion(self, x, y, dx, dy):
        # Mover icono de sonido
        if self.drag_sound:
            self.sound_icon.center_x = max(self.sound_bar.left, min(self.sound_bar.right, x))
            self.window.sound_bar = self.sound_icon.center_x
            self.sound_volume = (self.sound_icon.center_x - 170) / (330 - 170)
            self.window.sound_volume = self.sound_volume

        # Mover icono de música
        if self.drag_music:
            self.music_icon.center_x = max(self.music_bar.left, min(self.music_bar.right, x))
            self.window.music_bar = self.music_icon.center_x
            self.music_volume = (self.music_icon.center_x - 170) / (330 - 170)
            self.window.music_volume = self.music_volume
            self.window.music_bg.volume = self.window.music_volume

        if self.back.collides_with_point((x,y)):
            if not self.back.hovered:
                self.back.play_sound = arcade.play_sound(self.back.load_sound,self.window.sound_volume)
                self.back.hovered = True
            self.back.texture = self.back.img_hover
        else:
            self.back.texture = self.back.img_idle
            self.back.hovered = False

    def on_mouse_release(self, x, y, button, modifiers):
        if self.drag_sound:
            self.drag_sound = False

        if self.drag_music:
            self.drag_music = False