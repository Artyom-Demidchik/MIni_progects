import Cube
# staps = white_cross, full_white_cross, first_layer, second_layer, yellow_cross, corners_3_l, yellow_side, third_layer
# byyyworrwyybwgbworoobroggborbbrrwggooryobyggwgwybywrgw
# wwwwwwwwwgggggggggooooooooorrrrrrrrrbbbbbbbbbyyyyyyyyy
cube = Cube.RubiksCube()
cube.distribute_colors(list(input('Enter your scramble -> ')))
cube.print_cube()

white_cross = bool

total = 0
while white_cross:
    white_cross = (cube.cube[0][0][1] == 'w' and cube.cube[0][1][0] == 'w' and cube.cube[0][1][2] == 'w' and
                   cube.cube[0][2][1] == 'w')
    if white_cross:
        cube.L_clockwise_rotation(1)
        total += 1
print(total)




full_white_cross = ['wg', 'wo', 'wb', 'wr']
first_layer = ['wro', 'wob', 'wbr', 'wrg']
second_layer = ['go', 'ob', 'br', 'rg']
yellow_cross = ['y', 'y', 'y', 'y']
corners_3_l = ['go', 'ob', 'br', 'rg']
yellow_side = ['y', 'y', 'y', 'y']
third_layer = ['yg', 'yo', 'yb', 'yr']