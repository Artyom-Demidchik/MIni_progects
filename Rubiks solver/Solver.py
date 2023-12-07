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
    # Постановка бело-зелёного ребра

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


def installation_wo():
    # Постановка бело-оранжевого ребра

    # Проверка D[2][1]:w F[0][1]:o
    if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'o':
        return cube.cube
    elif cube.cube[5][2][1] != 'w' or cube.cube[1][0][1] != 'o':
        cube.L_counterclockwise_rotation(1)
        cube.D_counterclockwise_rotation(1)
        if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'o':
            solve_combination.append("L'")
            solve_combination.append("D'")
            cube.L_clockwise_rotation(1)
            solve_combination.append("L")
            return cube.cube
        elif cube.cube[5][2][1] != 'w' or cube.cube[1][0][1] != 'o':
            cube.D_counterclockwise_rotation(1)
            if cube.cube[5][2][1] == 'w' and cube.cube[1][0][1] == 'o':
                solve_combination.append("L'")
                solve_combination.append("D'2")
                cube.L_clockwise_rotation(1)
                solve_combination.append("L")
                return cube.cube
            elif cube.cube[5][2][1] != 'w' or cube.cube[1][0][1] != 'o':
                cube.D_counterclockwise_rotation(2)
                cube.L_clockwise_rotation(1)

    # Проверка D[2][1]:o F[0][1]:w
    if cube.cube[5][2][1] == 'o' and cube.cube[1][0][1] == 'w':
        cube.L_clockwise_rotation(1)
        solve_combination.append("L")
        cube.D_clockwise_rotation(1)
        solve_combination.append("D")
        cube.R_clockwise_rotation(1)
        solve_combination.append("R")
        cube.F_clockwise_rotation(1)
        solve_combination.append("F")
        cube.L_counterclockwise_rotation(1)
        solve_combination.append("L'")
        return cube.cube
    elif cube.cube[5][2][1] != 'o' or cube.cube[1][0][1] != 'w':
        cube.L_clockwise_rotation(1)
        cube.D_counterclockwise_rotation(1)
        if cube.cube[5][2][1] == 'o' and cube.cube[1][0][1] == 'w':
            solve_combination.append("L")
            solve_combination.append("D'")
            cube.D_clockwise_rotation(1)
            solve_combination.append("D")
            cube.R_clockwise_rotation(1)
            solve_combination.append("R")
            cube.F_clockwise_rotation(1)
            solve_combination.append("F")
            cube.L_counterclockwise_rotation(1)
            solve_combination.append("L'")
            return cube.cube
        elif cube.cube[5][2][1] != 'o' or cube.cube[1][0][1] != 'w':
            cube.D_counterclockwise_rotation(1)
            if cube.cube[5][2][1] == 'o' and cube.cube[1][0][1] == 'w':
                solve_combination.append("L")
                solve_combination.append("D'2")
                cube.D_clockwise_rotation(1)
                solve_combination.append("D")
                cube.R_clockwise_rotation(1)
                solve_combination.append("R")
                cube.F_clockwise_rotation(1)
                solve_combination.append("F")
                cube.L_counterclockwise_rotation(1)
                solve_combination.append("L'")
                return cube.cube
            elif cube.cube[5][2][1] != 'o' or cube.cube[1][0][1] != 'w':
                cube.D_counterclockwise_rotation(2)
                cube.L_counterclockwise_rotation(1)

    # Проверка F[1][2]:w R[1][0]:o
    if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'o':
        cube.D_clockwise_rotation(1)
        solve_combination.append("D")
        cube.R_counterclockwise_rotation(1)
        solve_combination.append("R'")
        cube.D_counterclockwise_rotation(1)
        solve_combination.append("D'")
        return cube.cube
    elif cube.cube[1][1][2] != 'w' or cube.cube[3][1][0] != 'o':
        cube.horizontal_clockwise_spin(1)
        if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'o':
            solve_combination.append('h')
            cube.D_clockwise_rotation(2)
            solve_combination.append("D2")
            cube.R_counterclockwise_rotation(1)
            solve_combination.append("R'")
            cube.D_counterclockwise_rotation(2)
            solve_combination.append("D'2")
            cube.horizontal_counterclockwise_spin(1)
            solve_combination.append("h'")
            return cube.cube
        elif cube.cube[1][1][2] != 'w' or cube.cube[3][1][0] != 'o':
            cube.horizontal_clockwise_spin(1)
            if cube.cube[1][1][2] == 'w' and cube.cube[3][1][0] == 'o':
                solve_combination.append('h2')
                cube.D_counterclockwise_rotation(1)
                solve_combination.append("D'")
                cube.R_counterclockwise_rotation(1)
                solve_combination.append("R'")
                cube.D_clockwise_rotation(1)
                solve_combination.append("D")
                cube.horizontal_counterclockwise_spin(2)
                solve_combination.append("h'2")
                return cube.cube
            elif cube.cube[1][1][2] != 'w' or cube.cube[3][1][0] != 'o':
                cube.horizontal_clockwise_spin(2)

    # Проверка F[1][2]:o R[1][0]:w
    if cube.cube[1][1][2] == 'o' and cube.cube[3][1][0] == 'w':
        cube.F_clockwise_rotation(1)
        solve_combination.append("F")
        return cube.cube
    elif cube.cube[1][1][2] != 'o' or cube.cube[3][1][0] != 'w':
        cube.horizontal_clockwise_spin(1)
        if cube.cube[1][1][2] == 'o' and cube.cube[3][1][0] == 'w':
            solve_combination.append("h")
            cube.D_clockwise_rotation(1)
            solve_combination.append("D")
            cube.F_clockwise_rotation(1)
            solve_combination.append("F")
            cube.D_counterclockwise_rotation(1)
            solve_combination.append("D'")
            cube.horizontal_counterclockwise_spin(1)
            solve_combination.append("h'")
            return cube.cube
        elif cube.cube[1][1][2] != 'o' or cube.cube[3][1][0] != 'w':
            cube.horizontal_clockwise_spin(1)
            if cube.cube[1][1][2] == 'o' and cube.cube[3][1][0] == 'w':
                solve_combination.append("h2")
                cube.D_clockwise_rotation(2)
                solve_combination.append("D2")
                cube.F_clockwise_rotation(1)
                solve_combination.append("F")
                cube.D_counterclockwise_rotation(2)
                solve_combination.append("D'2")
                cube.horizontal_counterclockwise_spin(2)
                solve_combination.append("h'2")
                return cube.cube
            elif cube.cube[1][1][2] != 'o' or cube.cube[3][1][0] != 'w':
                cube.horizontal_clockwise_spin(1)
                if cube.cube[1][1][2] == 'o' and cube.cube[3][1][0] == 'w':
                    solve_combination.append("h'")
                    cube.F_clockwise_rotation(1)
                    solve_combination.append("F")
                    cube.D_clockwise_rotation(1)
                    solve_combination.append("D")
                    cube.F_counterclockwise_rotation(1)
                    solve_combination.append("F'")
                    cube.horizontal_clockwise_spin(1)
                    solve_combination.append("h")
                    return cube.cube
                elif cube.cube[1][1][2] != 'o' or cube.cube[3][1][0] != 'w':
                    cube.horizontal_clockwise_spin(1)

    # Проверка F[2][1]:o U[0][1]:w
    if cube.cube[1][2][1] == 'o' and cube.cube[0][0][1] == 'w':
        cube.F_clockwise_rotation(2)
        solve_combination.append("F2")
        return cube.cube
    elif cube.cube[1][2][1] != 'o' or cube.cube[0][0][1] != 'w':
        cube.U_clockwise_rotation(1)
        if cube.cube[1][2][1] == 'o' and cube.cube[0][0][1] == 'w':
            solve_combination.append("U")
            cube.F_clockwise_rotation(2)
            solve_combination.append("F2")
            return cube.cube
        elif cube.cube[1][2][1] != 'o' or cube.cube[0][0][1] != 'w':
            cube.U_clockwise_rotation(1)
            if cube.cube[1][2][1] == 'o' and cube.cube[0][0][1] == 'w':
                solve_combination.append("U2")
                cube.F_clockwise_rotation(2)
                solve_combination.append("F2")
                return cube.cube
            elif cube.cube[1][2][1] != 'o' or cube.cube[0][0][1] != 'w':
                cube.U_clockwise_rotation(1)
                if cube.cube[1][2][1] == 'o' and cube.cube[0][0][1] == 'w':
                    solve_combination.append("U'")
                    cube.F_clockwise_rotation(2)
                    solve_combination.append("F2")
                    return cube.cube
                elif cube.cube[1][2][1] != 'o' or cube.cube[0][0][1] != 'w':
                    cube.U_clockwise_rotation(1)

    # Проверка F[2][1]:w U[0][1]:o
    if cube.cube[1][2][1] == 'w' and cube.cube[0][0][1] == 'o':
        cube.F_clockwise_rotation(1)
        solve_combination.append("F")
        cube.D_clockwise_rotation(1)
        solve_combination.append("D")
        cube.R_counterclockwise_rotation(1)
        solve_combination.append("R'")
        cube.D_counterclockwise_rotation(1)
        solve_combination.append("D'")
        return cube.cube
    elif cube.cube[1][2][1] != 'w' or cube.cube[0][0][1] != 'o':
        cube.U_clockwise_rotation(1)
        if cube.cube[1][2][1] == 'w' and cube.cube[0][0][1] == 'o':
            solve_combination.append("U")
            cube.F_clockwise_rotation(1)
            solve_combination.append("F")
            cube.D_clockwise_rotation(1)
            solve_combination.append("D")
            cube.R_counterclockwise_rotation(1)
            solve_combination.append("R'")
            cube.D_counterclockwise_rotation(1)
            solve_combination.append("D'")
            return cube.cube
        elif cube.cube[1][2][1] != 'w' or cube.cube[0][0][1] != 'o':
            cube.U_clockwise_rotation(1)
            if cube.cube[1][2][1] == 'w' and cube.cube[0][0][1] == 'o':
                solve_combination.append("U2")
                cube.F_clockwise_rotation(1)
                solve_combination.append("F")
                cube.D_clockwise_rotation(1)
                solve_combination.append("D")
                cube.R_counterclockwise_rotation(1)
                solve_combination.append("R'")
                cube.D_counterclockwise_rotation(1)
                solve_combination.append("D'")
                return cube.cube
            elif cube.cube[1][2][1] != 'w' or cube.cube[0][0][1] != 'o':
                cube.U_clockwise_rotation(1)
                if cube.cube[1][2][1] == 'w' and cube.cube[0][0][1] == 'o':
                    solve_combination.append("U'")
                    cube.F_clockwise_rotation(1)
                    solve_combination.append("F")
                    cube.D_clockwise_rotation(1)
                    solve_combination.append("D")
                    cube.R_counterclockwise_rotation(1)
                    solve_combination.append("R'")
                    cube.D_counterclockwise_rotation(1)
                    solve_combination.append("D'")
                    return cube.cube
                elif cube.cube[1][2][1] != 'w' or cube.cube[0][0][1] != 'o':
                    cube.U_clockwise_rotation(1)


installation_wg()

cube.horizontal_clockwise_spin(1)
solve_combination.append("h")
cube.F_clockwise_rotation(2)
cube.U_clockwise_rotation(2)
installation_wo()

print(solve_combination, end='\n'*2)
cube.print_cube()
