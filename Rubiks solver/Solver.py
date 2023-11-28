import Cube

# byyyworrwyybwgbworoobroggborbbrrwggooryobyggwgwybywrgw
# wwwwwwwwwgggggggggooooooooorrrrrrrrrbbbbbbbbbyyyyyyyyy
cube = Cube.RubiksCube()
cube.distribute_colors(list(input('Enter your scramble -> ')))
cube.vertical_clockwise_spin(2)
cube.horizontal_clockwise_spin(2)
cube.print_cube()
white_cross = ['wg', 'wo', 'wb', 'wr']
first_layer = ['wro', 'wob', 'wbr', 'wrg']
second_layer = ['go', 'ob', 'br', 'rg']
yellow_cross = ['y', 'y', 'y', 'y']
corners_3_l = ['go', 'ob', 'br', 'rg']
yellow_side = ['y', 'y', 'y', 'y']
third_layer = ['yg', 'yo', 'yb', 'yr']
staps = [white_cross, first_layer, second_layer, yellow_cross, corners_3_l,
         yellow_side, third_layer]
solve_combination = []


def installation_wg(cube):
    # Проверка D[2][1]:w F[0][1]:g
    if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'g':
        white_cross[0] = 1
    else:
        solve_combination.append("D'")
        cube.D_counterclockwise_spin(1)
        if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'g':
            white_cross[0] = 1
        else:
            solve_combination.append("D'")
            cube.D_counterclockwise_spin(1)
            if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'g':
                white_cross[0] = 1
            else:
                solve_combination.append("D'")
                cube.D_counterclockwise_spin(1)
                if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'g':
                    white_cross[0] = 1

    # Проверка D[2][1]:g F[0][1]:w
    if cube.cube[5][2][1] == 'g' and cube.cube[1][0][1] == 'w':
        cube.D_clockwise_spin(1)
        solve_combination.append("D")
        cube.R_clockwise_spin(1)
        solve_combination.append("R")
        cube.F_clockwise_spin(1)
        solve_combination.append("F")
        white_cross[0] = 1
    else:
        cube.D_counterclockwise_spin(1)
        solve_combination.append("D'")
        if cube.cube[5][2][1] == 'g' and cube.cube[1][0][1] == 'w':
            cube.D_clockwise_spin(1)
            solve_combination.append("D")
            cube.R_clockwise_spin(1)
            solve_combination.append("R")
            cube.F_clockwise_spin(1)
            solve_combination.append("F")
            white_cross[0] = 1
        else:
            cube.D_counterclockwise_spin(1)
            solve_combination.append("D'")
            if cube.cube[5][2][1] == 'g' and cube.cube[1][0][1] == 'w':
                cube.D_clockwise_spin(1)
                solve_combination.append("D")
                cube.R_clockwise_spin(1)
                solve_combination.append("R")
                cube.F_clockwise_spin(1)
                solve_combination.append("F")
                white_cross[0] = 1
            else:
                cube.D_counterclockwise_spin(1)
                solve_combination.append("D'")
                if cube.cube[5][2][1] == 'g' and cube.cube[1][0][1] == 'w':
                    cube.D_clockwise_spin(1)
                    solve_combination.append("D")
                    cube.R_clockwise_spin(1)
                    solve_combination.append("R")
                    cube.F_clockwise_spin(1)
                    solve_combination.append("F")
                    white_cross[0] = 1

    # Проверка F[1][2]:w R[1][0]:g
    if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'g':
        cube.R_counterclockwise_spin(1)
        solve_combination.append("R'")
        cube.D_counterclockwise_spin(1)
        solve_combination.append("D'")
        white_cross[0] = 1
    else:
        cube.horizontal_spin(1)
        solve_combination.append('h')
        if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'g':
            cube.R_counterclockwise_spin(1)
            solve_combination.append("R'")
            cube.D_counterclockwise_spin(2)
            solve_combination.append("D'2")
            white_cross[0] = 1
        else:
            cube.horizontal_spin(1)
            solve_combination.append('h')
            if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'g':
                cube.R_counterclockwise_spin(1)
                solve_combination.append("R'")
                cube.D_clockwise_spin(1)
                solve_combination.append("D")
                white_cross[0] = 1
            else:
                cube.horizontal_spin(1)
                solve_combination.append('h')
                if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'g':
                    cube.R_counterclockwise_spin(1)
                    solve_combination.append("R'")
                    white_cross[0] = 1

    # Проверка F[1][2]:g R[1][0]:w
