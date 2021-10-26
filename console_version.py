"""
Name: tic-tac-toe (console version)
ToDo:
    Map for valid moves - DONE
    Reverse 1-9 input to match numpad - DONE
    Add win counter, and play again option. - DONE

"""

import random as ran

game_board = [[' ' for _ in range(3)] for _ in range(3)]
map_board = [[x + y for y in range(3)] for x in range(1, 9, 3)]
valid_moves = [x for x in range(1, 10)]
p1_piece = 'X'
p2_piece = 'O'
move_counter = 0
# p1_pieces_on_board = set()
# p2_pieces_on_board = set()
win_conditions = [{0, 1, 2}, {3, 4, 5},
                  {6, 7, 8}, {0, 3, 6},
                  {1, 4, 7}, {2, 5, 8},
                  {0, 4, 8}, {2, 4, 6}]
p1_score = 0
p2_score = 0

# To match board with numpad layout
map_board.reverse()

# dict to match input with numpad layout
move_to_board_dict = dict()
counter = 1
for x in range(2, -1, -1):
    for y in range(3):
        move_to_board_dict[counter] = [x, y]
        counter += 1


def player_turn(move_count):
    if move_count % 2 == 0:
        player_piece = p1_piece
    else:
        player_piece = p2_piece
    return player_piece


def display_board(board_2d):
    text = ''
    for i, v in enumerate(board_2d):
        if i == 0:
            text += f'  ┌{"┬".join([("─" * 3) for _ in v])}┐\n'
        else:
            text += f'  ├{"┼".join([("─" * 3) for _ in v])}┤\n'
        text += f"{' '} │{'│'.join([str(x).center(3) for x in v])}│\n"

        if i == len(board_2d) - 1:
            text += f'  └{"┴".join([("─" * 3) for _ in v])}┘\n'
    return text


def get_player_move() -> int: 
    """Complains until a valid move is returned"""
    player_pick = 0
    while player_pick not in valid_moves:
        try:
            print(f'Current player: "{current_player}"')
            player_pick = int(input('Choose 1-9: '))
            if player_pick not in valid_moves:
                raise ValueError
        except ValueError:
            print(display_board(map_board))
            print(display_board(game_board))
            print('Try again! Valid moves: 1-9.')
    return player_pick


def insert_player_move(player_move, p1_board_pieces, p2_board_pieces):
    """Returns true if move is valid"""
    x, y = move_to_board_dict[player_move]
    if game_board[x][y] == ' ':
        game_board[x][y] = current_player

        if current_player == p1_piece:
            p1_board_pieces.add(player_move - 1)
        if current_player == p2_piece:
            p2_board_pieces.add(player_move - 1)
        return True
    else:
        print('Invalid move! Something has already been placed there.')
        print(display_board(map_board))
        print(display_board(game_board))



def win_check():
    """Returns true if win is detected"""
    for combination in win_conditions:
        if combination.issubset(p1_pieces_on_board) or combination.issubset(p2_pieces_on_board):
            return True


# game loop
if __name__ == '__main__':
    play_again = ''
    move_counter += ran.choice((0, 1))
    while play_again != 'no':
        play_again = ''
        p1_pieces_on_board = set()
        p2_pieces_on_board = set()
        game_board = [[' ' for _ in range(3)] for _ in range(3)]

        # move_counter += ran.choice((0, 1))
        print(display_board(map_board))

        for _ in range(9):
            current_player = player_turn(move_counter)
            move_counter += 1
            current_player_move = get_player_move()
            while not insert_player_move(current_player_move, p1_pieces_on_board, p2_pieces_on_board):
                current_player_move = get_player_move()
            print(display_board(map_board))
            print(display_board(game_board))
            if win_check():
                print(f'Player "{current_player}", wins!')
                if current_player == p1_piece:
                    p1_score +=1
                else:
                    p2_score +=1    
                break

        if not win_check():
            print('Draw!')
        # print('Game finished!')
        print('Score:')
        print(f'''"{p1_piece}": {p1_score}\n"{p2_piece}": {p2_score} ''')


        while play_again not in ('yes', 'no'):
            play_again = input('Want to play again? yes/no\n').lower().strip()
            if play_again not in ('yes', 'no'):
                print('Invalid choice! Try again.')
    print(
        f'''The final score is:
    {p1_piece}: {p1_score}
    {p2_piece}: {p2_score}\n'''
        )


