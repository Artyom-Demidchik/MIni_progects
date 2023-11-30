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


def installation_wg():
    # Проверка D[2][1]:w F[0][1]:g
    if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'g':
        return cube.cube
    elif cube.cube[5][2][1] != 'w' or cube.cube[1][0][1] != 'g':
        cube.D_counterclockwise_rotation(1)
        if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'g':
            solve_combination.append("D'")
            return cube.cube
        elif cube.cube[5][2][1] != 'w' or cube.cube[1][0][1] != 'g':
            cube.D_counterclockwise_rotation(1)
            if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'g':
                solve_combination.append("D'2")
                return cube.cube
            elif cube.cube[5][2][1] != 'w' or cube.cube[1][0][1] != 'g':
                cube.D_counterclockwise_rotation(1)
                if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'g':
                    solve_combination.append("D'")
                    return cube.cube
                elif cube.cube[5][2][1] != 'w' or cube.cube[1][0][1] != 'g':
                    cube.D_counterclockwise_rotation(1)

    # Проверка D[2][1]:g F[0][1]:w
    if cube.cube[5][2][1] == 'g' and cube.cube[1][0][1] == 'w':
        cube.D_clockwise_rotation(1)
        solve_combination.append("D")
        cube.R_clockwise_rotation(1)
        solve_combination.append("R")
        cube.F_clockwise_rotation(1)
        solve_combination.append("F")
        return cube.cube
    elif cube.cube[5][2][1] != 'g' or cube.cube[1][0][1] != 'w':
        cube.D_counterclockwise_rotation(1)
        if cube.cube[5][2][1] == 'g' and cube.cube[1][0][1] == 'w':
            solve_combination.append("D'")
            cube.D_clockwise_rotation(1)
            solve_combination.append("D")
            cube.R_clockwise_rotation(1)
            solve_combination.append("R")
            cube.F_clockwise_rotation(1)
            solve_combination.append("F")
            return cube.cube
        elif cube.cube[5][2][1] != 'g' or cube.cube[1][0][1] != 'w':
            cube.D_counterclockwise_rotation(1)
            if cube.cube[5][2][1] == 'g' and cube.cube[1][0][1] == 'w':
                solve_combination.append("D'2")
                cube.D_clockwise_rotation(1)
                solve_combination.append("D")
                cube.R_clockwise_rotation(1)
                solve_combination.append("R")
                cube.F_clockwise_rotation(1)
                solve_combination.append("F")
                return cube.cube
            elif cube.cube[5][2][1] != 'g' or cube.cube[1][0][1] != 'w':
                cube.D_counterclockwise_rotation(1)
                if cube.cube[5][2][1] == 'g' and cube.cube[1][0][1] == 'w':
                    solve_combination.append("D")
                    cube.D_clockwise_rotation(1)
                    solve_combination.append("D")
                    cube.R_clockwise_rotation(1)
                    solve_combination.append("R")
                    cube.F_clockwise_rotation(1)
                    solve_combination.append("F")
                    return cube.cube
                elif cube.cube[5][2][1] != 'g' or cube.cube[1][0][1] != 'w':
                    cube.D_counterclockwise_rotation(1)

    # Проверка F[1][2]:w R[1][0]:g
    if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'g':
        cube.R_counterclockwise_rotation(1)
        solve_combination.append("R'")
        cube.D_counterclockwise_rotation(1)
        solve_combination.append("D'")
        return cube.cube
    elif cube.cube[1][1][2] != 'w' or cube.cube[3][1][0] != 'g':
        cube.horizontal_clockwise_spin(1)
        if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'g':
            solve_combination.append('h')
            cube.R_counterclockwise_rotation(1)
            solve_combination.append("R'")
            cube.D_counterclockwise_rotation(2)
            solve_combination.append("D'2")
            return cube.cube
        elif cube.cube[1][1][2] != 'w' or cube.cube[3][1][0] != 'g':
            cube.horizontal_clockwise_spin(1)
            if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'g':
                solve_combination.append('h2')
                cube.R_counterclockwise_rotation(1)
                solve_combination.append("R'")
                cube.D_clockwise_rotation(1)
                solve_combination.append("D")
                return cube.cube
            elif cube.cube[1][1][2] != 'w' or cube.cube[3][1][0] != 'g':
                cube.horizontal_clockwise_spin(1)
                if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'g':
                    solve_combination.append("h'")
                    cube.R_counterclockwise_rotation(1)
                    solve_combination.append("R'")
                    return cube.cube
                elif cube.cube[1][1][2] != 'w' or cube.cube[3][1][0] != 'g':
                    cube.horizontal_clockwise_spin(1)

    # Проверка F[1][2]:g R[1][0]:w
    if cube.cube[1][1][2] == 'g' and cube.cube[3][1][0] == 'w':
        cube.F_clockwise_rotation(1)
        solve_combination.append("F")
        return cube.cube
    elif cube.cube[1][1][2] != 'g' or cube.cube[3][1][0] != 'w':
        cube.horizontal_clockwise_spin(1)
        if cube.cube[1][1][2] == 'g' and cube.cube[3][1][0] == 'w':
            solve_combination.append("h")
            cube.F_clockwise_rotation(1)
            solve_combination.append("F")
            cube.D_counterclockwise_rotation(1)
            solve_combination.append("D'")
            return cube.cube
        elif cube.cube[1][1][2] != 'g' or cube.cube[3][1][0] != 'w':
            cube.horizontal_clockwise_spin(1)
            if cube.cube[1][1][2] == 'g' and cube.cube[3][1][0] == 'w':
                solve_combination.append("h2")
                cube.F_clockwise_rotation(1)
                solve_combination.append("F")
                cube.D_counterclockwise_rotation(2)
                solve_combination.append("D'2")
                return cube.cube
            elif cube.cube[1][1][2] != 'g' or cube.cube[3][1][0] != 'w':
                cube.horizontal_clockwise_spin(1)
                if cube.cube[1][1][2] == 'g' and cube.cube[3][1][0] == 'w':
                    solve_combination.append("h'")
                    cube.F_clockwise_rotation(1)
                    solve_combination.append("F")
                    cube.D_clockwise_rotation(1)
                    solve_combination.append("D")
                    return cube.cube
                elif cube.cube[1][1][2] != 'g' or cube.cube[3][1][0] != 'w':
                    cube.horizontal_clockwise_spin(1)

    # Проверка F[2][1]:g U[0][1]:w
    if cube.cube[1][2][1] == 'g' and cube.cube[0][0][1] == 'w':
        cube.F_clockwise_rotation(2)
        solve_combination.append("F2")
        return cube.cube
    elif cube.cube[1][2][1] != 'g' or cube.cube[0][0][1] != 'w':
        cube.U_clockwise_rotation(1)
        if cube.cube[1][2][1] == 'g' and cube.cube[0][0][1] == 'w':
            solve_combination.append("U")
            cube.F_clockwise_rotation(2)
            solve_combination.append("F2")
            return cube.cube
        elif cube.cube[1][2][1] != 'g' or cube.cube[0][0][1] != 'w':
            cube.U_clockwise_rotation(1)
            if cube.cube[1][2][1] == 'g' and cube.cube[0][0][1] == 'w':
                solve_combination.append("U2")
                cube.F_clockwise_rotation(2)
                solve_combination.append("F2")
                return cube.cube
            elif cube.cube[1][2][1] != 'g' or cube.cube[0][0][1] != 'w':
                cube.U_clockwise_rotation(1)
                if cube.cube[1][2][1] == 'g' and cube.cube[0][0][1] == 'w':
                    solve_combination.append("U'")
                    cube.F_clockwise_rotation(2)
                    solve_combination.append("F2")
                    return cube.cube
                elif cube.cube[1][2][1] != 'g' or cube.cube[0][0][1] != 'w':
                    cube.U_clockwise_rotation(1)

    # Проверка F[2][1]:w U[0][1]:g
    if cube.cube[1][2][1] == 'w' and cube.cube[0][0][1] == 'g':
        cube.F_clockwise_rotation(1)
        solve_combination.append("F")
        cube.R_counterclockwise_rotation(1)
        solve_combination.append("R'")
        cube.D_counterclockwise_rotation(1)
        solve_combination.append("D'")
        return cube.cube
    elif cube.cube[1][2][1] != 'w' or cube.cube[0][0][1] != 'g':
        cube.U_clockwise_rotation(1)
        if cube.cube[1][2][1] == 'w' and cube.cube[0][0][1] == 'g':
            solve_combination.append("U")
            cube.F_clockwise_rotation(1)
            solve_combination.append("F")
            cube.R_counterclockwise_rotation(1)
            solve_combination.append("R'")
            cube.D_counterclockwise_rotation(1)
            solve_combination.append("D'")
            return cube.cube
        elif cube.cube[1][2][1] != 'w' or cube.cube[0][0][1] != 'g':
            cube.U_clockwise_rotation(1)
            if cube.cube[1][2][1] == 'w' and cube.cube[0][0][1] == 'g':
                solve_combination.append("U2")
                cube.F_clockwise_rotation(1)
                solve_combination.append("F")
                cube.R_counterclockwise_rotation(1)
                solve_combination.append("R'")
                cube.D_counterclockwise_rotation(1)
                solve_combination.append("D'")
                return cube.cube
            elif cube.cube[1][2][1] != 'w' or cube.cube[0][0][1] != 'g':
                cube.U_clockwise_rotation(1)
                if cube.cube[1][2][1] == 'w' and cube.cube[0][0][1] == 'g':
                    solve_combination.append("U'")
                    cube.F_clockwise_rotation(1)
                    solve_combination.append("F")
                    cube.R_counterclockwise_rotation(1)
                    solve_combination.append("R'")
                    cube.D_counterclockwise_rotation(1)
                    solve_combination.append("D'")
                    return cube.cube
                elif cube.cube[1][2][1] != 'w' or cube.cube[0][0][1] != 'g':
                    cube.U_clockwise_rotation(1)



installation_wg()
print(solve_combination)
