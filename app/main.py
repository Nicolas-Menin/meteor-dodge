import arcade
from config import WIDTH,HEIGHT
from window import GameWindow

def main():
    """Se instancia la ventana y corre el juego"""
    window = GameWindow(WIDTH,HEIGHT,"arcade")
    menu = window.game_over_view
    menu.setup()
    window.show_view(menu)
    arcade.run()

if __name__ == "__main__":

    main()



