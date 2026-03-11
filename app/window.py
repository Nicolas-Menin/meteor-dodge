import arcade
from views.configure_views import ConfigurationView
from views.main_menu_screen import MainMenuView
from views.game_views import GameView
from views.game_over_views import GameOverView


class GameWindow(arcade.Window):

    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.center_window()
        self.music_volume = 0.5
        self.sound_volume = 0.5
        self.music_bar = 250
        self.sound_bar = 250
        self.music_load= arcade.load_sound("app/music/Music.wav")
        self.explosion_sound = arcade.load_sound("app/sfx/Explosion.wav")
        self.music_bg = arcade.play_sound(self.music_load,volume=self.sound_volume,loop=True)
        self.button_sound = arcade.load_sound("app/sfx/button.wav")
        self.ufo_warble = arcade.load_sound("app/sfx/UFO_warble.wav")
        self.game_over_sound = arcade.load_sound("app/sfx/GameOver.wav")
        self.collectable_sound = arcade.load_sound("app/sfx/CollectableSound.wav")
        arcade.load_font("app/font/PublicPixel.ttf")

        # Views
        self.game_view = GameView()
        self.main_menu_view = MainMenuView()
        self.configuration_view = ConfigurationView()
        self.game_over_view = GameOverView()

