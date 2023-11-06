# byyyworrwyybwgbworoobroggborbbrrwggooryobyggwgwybywrgw
white_side = [[0] * 3 for _ in range(3)]
green_side = [[0] * 3 for _ in range(3)]
orange_side = [[0] * 3 for _ in range(3)]
red_side = [[0] * 3 for _ in range(3)]
blue_side = [[0] * 3 for _ in range(3)]
yellow_side = [[0] * 3 for _ in range(3)]
scramble = [white_side, green_side, orange_side, red_side, blue_side, yellow_side]
person_scramble = list(input('Enter your scramble -> '))

for i in range(6):
    for j in range(3):
        for h in range(3):
            scramble[i][j][h] = person_scramble.pop(0)


def search_white_color(side):
    for layer in yellow_side:
        for color in layer:
            if color == 'w':
                return


print(search_white_color(yellow_side))
