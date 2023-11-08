# byyyworrwyybwgbworoobroggborbbrrwggooryobyggwgwybywrgw
# wwwwwwwwwgggggggggooooooooorrrrrrrrrbbbbbbbbbyyyyyyyyy
# r - horizontal spins
# R - right side spins
# L - left side spins
# F - front side spins
# B - back side spins
# U - up side spins
# D - down side spins

white_side = [[0] * 3 for _ in range(3)]
green_side = [[0] * 3 for _ in range(3)]
orange_side = [[0] * 3 for _ in range(3)]
red_side = [[0] * 3 for _ in range(3)]
blue_side = [[0] * 3 for _ in range(3)]
yellow_side = [[0] * 3 for _ in range(3)]
cube = [white_side, green_side, orange_side, red_side, blue_side, yellow_side]
person_scramble = list(input('Enter your scramble -> '))

for i in range(6):
    for j in range(3):
        for h in range(3):
            cube[i][j][h] = person_scramble.pop(0)


def rotate_clockwise(side):
    # Поворот стороны по часовой стрелке
    side[0], side[1], side[2] = [side[0][2],
                                 side[1][2],
                                 side[2][2]], [side[0][1],
                                               side[1][1],
                                               side[2][1]], [side[0][0],
                                                             side[1][0],
                                                             side[2][0]]



def rotate_counterclockwise(side):
    # Поворот стороны против часовой стрелки
    side[0], side[1], side[2] = [side[2][0],
                                 side[1][0],
                                 side[0][0]], [side[2][1],
                                               side[1][1],
                                               side[0][1]], [side[2][2],
                                                             side[1][2],
                                                             side[0][2]]




def R_rotation(cube):
    # Вращение правой стороны
    rotate_clockwise(cube[4])
    cube[0][0][2], cube[1][0][2], cube[2][0][0], cube[5][2][0] = cube[5][2][0], cube[0][0][2], cube[1][0][2], \
    cube[2][0][0]


def L_rotation(cube):
    # Вращение левой стороны
    rotate_clockwise(cube[3])
    cube[0][0][0], cube[1][0][0], cube[2][0][2], cube[5][2][2] = cube[5][2][2], cube[0][0][0], cube[1][0][0], \
    cube[2][0][2]


def B_rotation(cube):
    # Вращение задней стороны
    rotate_clockwise(cube[2])
    cube[0][0][2], cube[3][0][0], cube[1][0][0], cube[4][0][2] = cube[4][0][2], cube[0][0][2], cube[3][0][0], \
    cube[1][0][0]


def F_rotation(cube):
    # Вращение передней стороны
    rotate_clockwise(cube[1])
    cube[0][2][0], cube[3][2][2], cube[2][0][2], cube[4][2][0] = cube[4][2][0], cube[0][2][0], cube[3][2][2], \
    cube[2][0][2]


def U_rotation(cube):
    # Вращение верхней стороны
    rotate_clockwise(cube[0])
    cube[1][0][2], cube[2][0][0], cube[3][0][0], cube[4][0][0] = cube[4][0][0], cube[1][0][2], cube[2][0][0], \
    cube[3][0][0]


def D_rotation(cube):
    # Вращение нижней стороны
    rotate_clockwise(cube[5])
    cube[1][2][0], cube[2][2][2], cube[3][2][2], cube[4][2][2] = cube[4][2][2], cube[1][2][0], cube[2][2][2], \
    cube[3][2][2]


def horizontal_spin(r):
    for _ in range(r):

        rotate_clockwise(white_side)
        rotate_counterclockwise(yellow_side)
    return cube


def search_white_color(side):
    pass
    for layer in side:
        for color in layer:
            if color == 'w':
                return


print(*horizontal_spin(1), sep='\n')
