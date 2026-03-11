import arcade
from config import WIDTH,HEIGHT
from window import GameWindow

def main():
    """Se instancia la ventana y corre el juego"""
    window = GameWindow(WIDTH,HEIGHT,"arcade")
    menu = window.main_menu_view
    window.music_bg.play()
    menu.setup()
    window.show_view(menu)
    arcade.run()

if __name__ == "__main__":

    main()



