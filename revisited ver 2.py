import random


def get_winner(p1_choice, cpu_choice) -> int:
    """
    Returns 
    0 - draw
    1 - p1 win
    2 - cpu win
    """
    return [0, (p1_choice[0]+cpu_choice[0] in "rpsr")+1][p1_choice != cpu_choice]


def game_loop():
    p1_points = 0
    cpu_points = 0

    print('q for quit')
    while (p1_pick := input('Rock, Paper, scissors? ').lower().strip()) not in ['quit', 'q']:
        while p1_pick not in ['rock', 'paper', 'scissors', 'r', 'p', 's', 'quit', 'q']:
            print('Invalid choice!')
            p1_pick = input('Rock, Paper, scissors? ').lower().strip()

        if p1_pick in ['quit', 'q']:
            break
        if p1_pick in ['r', 'p', 's']:
            p1_pick = ['rock', 'paper', 'scissors'][('r', 'p', 's').index(p1_pick)]

        round_winner = get_winner(p1_pick, cpu_pick := random.choice(['rock', 'paper', 'scissors']))
        if round_winner == 0:
            winner_text = 'Draw'
        if round_winner == 1:
            winner_text = 'Player 1 wins!'
            p1_points += 1
        if round_winner == 2:
            winner_text = 'CPU wins!'
            cpu_points += 1
        
        print(
        '',
        'You picked ' + p1_pick,
        'CPU picked ' + cpu_pick,
        '',
        winner_text,
        '*** Score ***', 
        f'You: {p1_points}', 
        f'CPU: {cpu_points}', 
        sep='\n')
    print()
    print()
    print('Final Score:')
    print(f'You: {p1_points}')
    print(f'CPU: {cpu_points}')


if __name__ == '__main__':
    game_loop()
