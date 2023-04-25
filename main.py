import text_mode
import poker_gui

def main():

    #text_mode.text_mode()
    play_again = poker_gui.play()
    while play_again ==True:
        play_again = poker_gui.play()


main()