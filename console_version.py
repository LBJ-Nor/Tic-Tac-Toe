# tic-tac-toe console version
# To-Do:
# map for valid move
# Add win counter, and play again option.

board = [[' ' for _ in range(3)] for _ in range(3)]
valid_moves = [x for x in range(1, 10)]
p1_piece = 'X'
p2_piece = 'O'
move_counter = 0
p1_pieces_on_board = set()
p2_pieces_on_board = set()

win_conditions = [{0, 1, 2}, {3, 4, 5},
                  {6, 7, 8}, {0, 3, 6},
                  {1, 4, 7}, {2, 5, 8},
                  {0, 4, 8}, {2, 4, 6}]


def player_turn():
    global move_counter
    if move_counter % 2 == 0:
        player_piece = p1_piece
    else:
        player_piece = p2_piece
    move_counter += 1
    return player_piece


def display_board(board):
    text = ''
    for i, v in enumerate(board):
        if i == 0:
            text += f'  ┌{"┬".join([("─" * 3) for _ in v])}┐\n'
        else:
            text += f'  ├{"┼".join([("─" * 3) for _ in v])}┤\n'
        text += f"{' '} │{'│'.join([str(x).center(3) for x in v])}│\n"

        if i == len(board) - 1:
            text += f'  └{"┴".join([("─" * 3) for _ in v])}┘\n'
    return text


def get_player_move():
    player_pick = 0
    while player_pick not in valid_moves:
        try:
            player_pick = int(input('Choose 1-9: '))
            if player_pick not in valid_moves:
                raise ValueError
        except ValueError:
            print('Try again! Valid moves: 1-9.')
    return player_pick


def insert_player_move(player_move):
    global board, p1_pieces_on_board, p2_pieces_on_board
    # Using math to find correct index.
    if board[(((player_move + 2) // 3) - 1)][(player_move % 3) - 1] == ' ':
        board[(((player_move + 2) // 3) - 1)][(player_move % 3) - 1] = current_player
        if current_player == p1_piece:
            p1_pieces_on_board.add(player_move - 1)
        if current_player == p2_piece:
            p2_pieces_on_board.add(player_move - 1)
        return True
    else:
        print('Invalid move! Something has already been placed there.')
        return False


def win_check():
    global p1_pieces_on_board, p2_pieces_on_board
    for combination in win_conditions:
        if combination.issubset(p1_pieces_on_board) or combination.issubset(p2_pieces_on_board):
            return True


# game loop
if __name__ == '__main__':
    print(display_board(board))

    for _ in range(9):
        current_player = player_turn()
        current_player_move = get_player_move()
        while not insert_player_move(current_player_move):
            current_player_move = get_player_move()
        print(display_board(board))
        if win_check():
            print(current_player, 'wins!')
            break
    print('Game finished!')
    if not win_check():
        print('Draw!')
