# byyyworrwyybwgbworoobroggborbbrrwggooryobyggwgwybywrgw
# wwwwwwwwwgggggggggooooooooorrrrrrrrrbbbbbbbbbyyyyyyyyy
# r - horizontal spins
# v - vertical spins
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

# Вывод Куба
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
    return side


def rotate_counterclockwise(side):
    # Поворот стороны против часовой стрелки
    side[0], side[1], side[2] = [side[2][0],
                                 side[1][0],
                                 side[0][0]], [side[2][1],
                                               side[1][1],
                                               side[0][1]], [side[2][2],
                                                             side[1][2],
                                                             side[0][2]]
    return side


def R_rotation(R):
    # Вращение правой стороны
    for _ in range(R):
        rotate_clockwise(cube[3])
        cube[0][0][2], cube[0][1][2], cube[0][2][2], \
            cube[1][0][2], cube[1][1][2], cube[1][2][2], \
            cube[4][0][0], cube[4][1][0], cube[4][2][0], \
            cube[5][0][2], cube[5][1][2], cube[5][2][2] \
            = \
            cube[1][0][2], cube[1][1][2], cube[1][2][2], \
            cube[5][0][2], cube[5][1][2], cube[5][2][2], \
            cube[0][2][2], cube[0][1][2], cube[0][0][2], \
            cube[4][0][0], cube[4][1][0], cube[4][2][0]
    return cube


def L_rotation(L):
    # Вращение левой стороны
    for _ in range(L):
        rotate_clockwise(cube[2])
        cube[0][0][0], cube[0][1][0], cube[0][2][0], \
            cube[1][0][0], cube[1][1][0], cube[1][2][0], \
            cube[4][0][2], cube[4][1][2], cube[4][2][2], \
            cube[5][0][0], cube[5][1][0], cube[5][2][0] \
            = \
            cube[4][2][2], cube[4][1][2], cube[4][0][2], \
            cube[0][0][0], cube[0][1][0], cube[0][2][0], \
            cube[5][2][0], cube[5][1][0], cube[5][0][0], \
            cube[1][0][0], cube[1][1][0], cube[1][2][0]
    return cube


def B_rotation(B):
    # Вращение задней стороны
    for _ in range(B):
        rotate_clockwise(cube[4])
        cube[0][2][0], cube[0][2][1], cube[0][2][2], \
            cube[2][0][0], cube[2][1][0], cube[2][2][0], \
            cube[3][0][2], cube[3][1][2], cube[3][2][2], \
            cube[5][0][0], cube[5][0][1], cube[5][0][2] \
            = \
            cube[3][2][2], cube[3][1][2], cube[3][0][2], \
            cube[0][2][0], cube[0][2][1], cube[0][2][2], \
            cube[5][0][0], cube[5][0][1], cube[5][0][2], \
            cube[2][2][0], cube[2][1][0], cube[2][0][0]
    return cube


def F_rotation(F):
    # Вращение передней стороны
    for _ in range(F):
        rotate_clockwise(cube[1])
        cube[0][0][0], cube[0][0][1], cube[0][0][2], \
            cube[2][0][2], cube[2][1][2], cube[2][2][2], \
            cube[3][0][0], cube[3][1][0], cube[3][2][0], \
            cube[5][2][0], cube[5][2][1], cube[5][2][2] \
            = \
            cube[2][0][2], cube[2][1][2], cube[2][2][2], \
            cube[5][2][2], cube[5][2][1], cube[5][2][0], \
            cube[0][0][2], cube[0][0][1], cube[0][0][0], \
            cube[3][0][0], cube[3][1][0], cube[3][2][0]
    return cube


def U_rotation(U):
    # Вращение верхней стороны
    for _ in range(U):
        rotate_clockwise(cube[0])
        cube[1][2], \
            cube[2][2], \
            cube[3][2], \
            cube[4][2] \
            = \
            cube[3][2], \
                cube[1][2], \
                cube[4][2], \
                cube[2][2]
    return cube


def D_rotation(D):
    # Вращение нижней стороны
    for _ in range(D):
        rotate_clockwise(cube[5])
        cube[1][0], \
            cube[2][0], \
            cube[3][0], \
            cube[4][0] \
            = \
            cube[2][0], \
            cube[4][0], \
            cube[1][0], \
            cube[3][0]
    return cube


def horizontal_spin(r):
    for _ in range(r):
        rotate_clockwise(cube[0])
        rotate_counterclockwise(cube[5])
        cube[1], cube[2], cube[3], cube[4] = cube[3], cube[1], cube[4], cube[2]
    return cube


def vertical_spin(v):
    for _ in range(v):
        rotate_clockwise(cube[3])
        rotate_counterclockwise(cube[2])
        cube[0], cube[1], cube[5], cube[4] = cube[1], cube[5], cube[4], cube[0]
    return cube


def search_white_color(side):
    pass
    for layer in side:
        for color in layer:
            if color == 'w':
                return


print(*vertical_spin(1), sep='\n')
