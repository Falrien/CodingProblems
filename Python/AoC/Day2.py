results = [[4, 1, 7], [8, 5, 2], [3, 9, 6]]


def get_opponent_index(opponent):
    match (opponent):
        case ('A'):
            return 0
        case ('B'):
            return 1
        case ('C'):
            return 2
        case _:
            print("No valid play found!")
            return -1


def get_player_index(player):
    match (player):
        case ('X'):
            return 0
        case ('Y'):
            return 1
        case ('Z'):
            return 2
        case _:
            print("No valid play found!")

def get_player_index2(player):
    match (player):
        case ('X'):
            return -1
        case ('Y'):
            return 0
        case ('Z'):
            return 1
        case _:
            print("No valid play found!")


def solve1():
    f = open('input.txt', 'r')
    score = 0
    for line in f:
        opponent_move, your_move = line.split()
        their_index = get_opponent_index(opponent_move)
        your_index = get_player_index(your_move)
        score += results[your_index][their_index]
    print(score)


def solve2():
    f = open('input.txt', 'r')
    score = 0
    for line in f:
        opponent_move, your_move = line.split()
        their_index = get_opponent_index(opponent_move)
        your_offset = get_player_index2(your_move)
        score += results[(their_index + your_offset) % 3][their_index]
    print(score)


if __name__ == '__main__':
    solve1()
    solve2()
