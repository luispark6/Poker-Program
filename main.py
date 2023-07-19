import text_mode
import poker_gui

def main():
    while True:
        try: #used so to take a valid input from user
            num_player = int(input(("Would you like to play in terminal(1) or on GUI(2) ")))
            x = int(num_player)
            if x==2 or x==1:
                break #breaks if valid1 int is inputted
        except:
            print("Please input an integer 1 or 2 ")

    if x ==1:
        text_mode.text_mode()
    else:

        play_again = poker_gui.play()
        while play_again ==True:
            play_again = poker_gui.play()


main()
