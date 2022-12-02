
CHOICE = { 'A': 1, 'B': 2, 'C': 3,
           'X': 1, 'Y': 2, 'Z': 3 }


WINNING_MOVE = { 'A': 'Y', 
                 'B': 'Z',
                 'C': 'X' }

LOSING_MOVE =  { 'A': 'C', 
                 'B': 'A',
                 'C': 'B' }

DRAWING_MOVE = { 'A': 'X', 
                 'B': 'Y',
                 'C': 'Z' }


# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

SCORE = { 'win': 6, 'draw': 3, 'lose': 0 }

def get_score(match):
    opponent_move = CHOICE[match[0]]
    own_move = CHOICE[match[1]]
    
    if opponent_move == own_move:
        return SCORE['draw'] + own_move
    elif opponent_move == 3 and own_move == 1:
        return SCORE['win'] + own_move
    elif opponent_move == 1 and own_move == 3:
        return SCORE['lose'] + own_move
    elif opponent_move > own_move:
        return SCORE['lose'] + own_move
    else:
        return SCORE['win'] + own_move


def get_move(match):
    opponent_move = match[0]
    required_result = match[1]
    if required_result == 'X':
        return LOSING_MOVE[opponent_move]
    if required_result == 'Y':
        return DRAWING_MOVE[opponent_move]
    if required_result == 'Z':
        return WINNING_MOVE[opponent_move]


if __name__ == '__main__':
    score = 0

    with open('input02.txt', 'rb') as f:
        matches = [s.split() for s in f.readlines()]

    for match in matches:
        move = get_move(match)
        score += get_score((match[0], move))

    print score
