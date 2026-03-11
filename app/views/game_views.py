import arcade
from entities.background import Background
from entities.collectables import Collectable
from entities.player import Player
from entities.enemy import Enemy
from config import MOVEMENT_SPEED
from ui.images import Images


class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.bg_list = None
        self.player_list = None
        self.collectables_list = None
        self.bg = None
        self.bg2 = None
        self.enemy_list = None
        self.enemy  = None
        self.player = None
        self.press_up = False
        self.press_down = False
        self.press_left = False
        self.press_right = False
        self.timer = 0
        self.enemy_count = 1
        self.paused = True
        self.pause_timer = 0
        self.game_over = None
        self.collectable = None
        self.alien_image = None
        self.count_alien = None
        self.text_count = None
        self.images_list = None
        self.can_move = None

    def setup(self):
        self.bg_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.images_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.collectables_list = arcade.SpriteList()
        self.collectable = Collectable("app/assets/Alien.png",3,5,10)
        self.alien_image = Images("app/assets/Alien.png",35,30)
        self.count_alien = 0
        self.text_count = arcade.Text(f":{self.count_alien}",x=50,y=20,color=arcade.color.WHITE,font_name="Public Pixel",font_size=15)
        self.can_move = True
        self.game_over = False
        self.bg = Background(750)
        self.bg2 = Background(2250)
        self.player = Player(self.window.ufo_warble)
        self.enemy_count = 1
        self.bg_list.append(self.bg)
        self.bg_list.append(self.bg2)
        self.player_list.append(self.player)
        self.collectables_list.append(self.collectable)
        self.images_list.append(self.alien_image)

    def on_show_view(self):
        pass

    def on_update(self, delta_time):


        self.bg_list.update(delta_time)
        self.enemy_list.update(delta_time)
        self.player_list.update(delta_time)
        self.collectables_list.update(delta_time)

        if self.enemy_count < 3:
            self.timer += delta_time
            if self.timer >= 5:
                self.enemy = Enemy(f"app/assets/Meteoritos_{self.enemy_count}.png")
                self.enemy_list.append(self.enemy)
                self.enemy_count +=1
                self.timer = 0


        if self.player.change_x != 0 or self.player.change_y != 0 :
            if self.player.warble_sound_play is None:
                self.player.warble_sound_play = arcade.play_sound(self.player.warble_sound_load,self.window.sound_volume,False)

        else:
            if self.player.warble_sound_play:
                arcade.stop_sound(self.player.warble_sound_play)
                self.player.warble_sound_play = None

        if arcade.check_for_collision_with_list(self.player,self.enemy_list):
            if not self.game_over:
                self.game_over = True
                arcade.play_sound(self.window.explosion_sound,self.window.sound_volume)
                self.timer = 0
            self.player.texture = arcade.load_texture("app/assets/Explosion.png")

        if self.game_over:
            self.timer += delta_time
            self.can_move = False
            if self.timer >= 2:
                arcade.stop_sound(self.window.music_bg)
                self.window.game_over_view.setup()
                self.window.show_view(self.window.game_over_view)

        if self.collectable.picked:
            self.collectable.timer = 0
            self.collectable.spawn()
            self.collectables_list.append(self.collectable)
            self.collectable.picked = False
            self.count_alien +=1
            self.text_count.text = f":{self.count_alien}"

        elif arcade.check_for_collision_with_list(self.player,self.collectables_list):
            arcade.play_sound(self.window.collectable_sound,self.window.sound_volume)
            self.collectables_list.remove(self.collectable)
            self.collectable.picked = True

    def on_draw(self):

        self.clear()

        self.bg_list.draw()
        self.enemy_list.draw()
        self.collectables_list.draw()
        self.player_list.draw()
        self.images_list.draw()
        self.text_count.draw()


    def update_player_speed(self):

        self.player.change_x = 0
        self.player.change_y = 0

        if self.press_up and not self.press_down:

            self.player.change_y = MOVEMENT_SPEED

        if self.press_down and not self.press_up:
            self.player.change_y = -MOVEMENT_SPEED

        if self.press_right and not self.press_left:
            self.player.change_x = MOVEMENT_SPEED

        if self.press_left and not self.press_right:
            self.player.change_x = -MOVEMENT_SPEED



    def on_key_press(self,symbol,modifiers):
        if not self.can_move:
            return
        if symbol == arcade.key.A:
            self.press_left = True

        if symbol == arcade.key.D:
            self.press_right = True

        if symbol == arcade.key.W:
            self.press_up = True


        if symbol == arcade.key.S:
            self.press_down = True


        self.update_player_speed()

    def on_key_release(self,symbol, modifiers):
        if symbol == arcade.key.A:
            self.press_left = False

        if symbol == arcade.key.D:
            self.press_right = False

        if symbol == arcade.key.W:
            self.press_up = False

        if symbol == arcade.key.S:
            self.press_down = False


        self.update_player_speed()
