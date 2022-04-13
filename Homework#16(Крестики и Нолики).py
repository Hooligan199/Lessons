game_result = [
    "OOX",
    "XXO",
    "OXX"]

# [
#     "X.O",
#     "XX.",
#     "XOO"] -> X

# [
#     "OO.",
#     "XOX",
#     "XOX"] -> O

# [
#     "OOX",
#     "XXO",
#     "OXX"] -> D

def checkio(game_result):
    for y in game_result:
        if y == 'XXX':
            return 'X'
        if y == 'OOO':
            return 'O'

    for y in range(3):
        if game_result[0][y] is game_result[1][y] is game_result[2][y]:
            return game_result[0][y]

    if game_result[0][0] is game_result[1][1] is game_result[2][2]:
        return game_result[0][0]

    if game_result[0][2] is game_result[1][1] is game_result[2][0]:
        return game_result[0][2]

    return 'D'


if __name__ == '__main__':
    print(checkio(game_result))

