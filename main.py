# Title: Tic-Tac-Toe/Connect Three
# Version: beta
# To-Do: Add win_check

import tkinter as tk

move_counter = 0
window = tk.Tk()
window.title('Tic-Tac-Toe')


# return player_piece as string.
def player_turn():
    global move_counter
    if move_counter % 2 == 0:
        player_piece = 'X'
    else:
        player_piece = 'O'
    move_counter += 1
    return player_piece


def move_validator(button_pressed):
    if button_pressed.cget('text') == '':
        button_pressed.config(text=player_turn())
    else:
        print('Invalid move!')


# Create buttons
buttons_list = []
for button in range(9):
    btn = tk.Button(window, text='',
                    borderwidth=1,
                    height=6,
                    width=18,
                    bg='#777777'
                    )
    btn.config(command=lambda button=button: buttons_list[button].config(text=move_validator(buttons_list[button])))
    buttons_list.append(btn)

# Place buttons by grid
counter = 0
for x in range(3):
    for y in range(3):
        buttons_list[counter].grid(row=x, column=y)
        counter += 1

window.mainloop()


