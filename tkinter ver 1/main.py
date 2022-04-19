# Title: Tic-Tac-Toe/Connect Three
# To-Do: Add win_check


import tkinter as tk

move_counter = 0
win_counter_X = 0
win_counter_O = 0

# window settings
window = tk.Tk()
window.title('Tic-Tac-Toe')
window.geometry('450x600')
window.config(bg='#222222')


# Check and count player turn
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


# frame for buttons
button_frame = tk.Frame(bg='#222222')
button_frame.pack(side=tk.TOP)

# Game text label
game_text = tk.Label(bg='#a39c87', width=60, height=10, )
game_text.pack(side=tk.TOP)

# Create buttons
buttons_list = []
for button in range(9):
    btn = tk.Button(button_frame,
                    text='',
                    height=2,
                    width=6,
                    bg='#777777',
                    font=('calibri', 30),
                    borderwidth=8,
                    activebackground='orange4'
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


