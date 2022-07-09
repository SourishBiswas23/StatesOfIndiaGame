from turtle import Screen
from pathlib import Path
import state_list
import reveal_states


STATE_LIST = []
STATE_COORDINATES = []
SCREEN_HEIGHT = 943
SCREEN_WIDTH = 800
IMAGE_NAME = "india_map.gif"
TITLE_OF_SCREEN = "Guess the states of India"
TEXT_OF_PROMPT = "Guess the name of a state"

script_folder = Path(__file__).absolute().parent
image_location = script_folder/IMAGE_NAME

my_screen = Screen()
my_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
my_screen.bgpic(image_location)
my_screen.title(TITLE_OF_SCREEN)

total_states = state_list.total_number_of_states()
correct_guesses = 0
while correct_guesses != total_states:
    guess = my_screen.textinput(
        title=f"Correct Guesses: {correct_guesses}/{total_states}", prompt=TEXT_OF_PROMPT).title()
    state_position = state_list.check_states(guess)
    if state_position == False:
        continue
    else:
        reveal_states.States(state_position, guess)
        correct_guesses += 1
    if correct_guesses == total_states:
        break


my_screen.mainloop()
