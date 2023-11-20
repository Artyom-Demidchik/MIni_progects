# byyyworrwyybwgbworoobroggborbbrrwggooryobyggwgwybywrgw
# wwwwwwwwwgggggggggooooooooorrrrrrrrrbbbbbbbbbyyyyyyyyy
# hc - horizontal clockwise cube spins →
# hcc - horizontal counterclockwise cube spins ←
# vc - vertical clockwise cube spins ↑
# vcc - vertical counterclockwise cube spins ↓
# Rc - right side clockwise spins
# Rcc - right side counterclockwise spins
# Lc - left side clockwise spins
# Lcc - left side counterclockwise spins
# Fc - front side clockwise spins
# Fcc - front side counterclockwise spins
# Bc - back side clockwise spins
# Bcc - back side counterclockwise spins
# Uc - up side clockwise spins
# Ucc - up side counterclockwise spins
# Dc - down side clockwise spins
# Dcc - down side counterclockwise spins

class RubiksCube:
    def __init__(self):
        self.white_side = [['w'] * 3 for _ in range(3)]
        self.green_side = [['g'] * 3 for _ in range(3)]
        self.orange_side = [['o'] * 3 for _ in range(3)]
        self.red_side = [['r'] * 3 for _ in range(3)]
        self.blue_side = [['b'] * 3 for _ in range(3)]
        self.yellow_side = [['y'] * 3 for _ in range(3)]
        self.cube = [self.white_side, self.green_side, self.orange_side, self.red_side, self.blue_side,
                     self.yellow_side]

    def distribute_colors(self, scramble):
        # Распределение цветов
        for i in range(6):
            for j in range(3):
                for h in range(3):
                    self.cube[i][j][h] = scramble.pop(0)

    def rotate_clockwise(self, side):
        # Поворот стороны по часовой стрелке
        side[0], side[1], side[2] = [side[0][2], side[1][2], side[2][2]], [side[0][1], side[1][1], side[2][1]], [
            side[0][0], side[1][0], side[2][0]]
        return side

    def rotate_counterclockwise(self, side):
        # Поворот стороны против часовой стрелки
        side[0], side[1], side[2] = [side[2][0], side[1][0], side[0][0]], [side[2][1], side[1][1], side[0][1]], [
            side[2][2], side[1][2], side[0][2]]
        return side

    def horizontal_clockwise_spin(self, hc):
        # Вращение куба по часовой стрелке →
        for _ in range(hc):
            self.rotate_clockwise(self.cube[0])
            self.rotate_counterclockwise(self.cube[5])
            self.cube[1], self.cube[2], self.cube[3], self.cube[4] = self.cube[3], self.cube[1], self.cube[4], \
                self.cube[2]
        return self.cube

    def horizontal_counterclockwise_spin(self, hcc):
        # Вращение куба против часовой стрелки ←
        for _ in range(hcc):
            self.horizontal_clockwise_spin(3)
        return self.cube

    def vertical_clockwise_spin(self, vc):
        # Вращение куба по часовой стрелке ↑
        for _ in range(vc):
            self.rotate_clockwise(self.cube[3])
            self.rotate_counterclockwise(self.cube[2])
            self.cube[0], self.cube[1], self.cube[5], self.cube[4] = self.cube[1], self.cube[5], self.cube[4], \
                self.cube[0]
            for _ in range(2):
                self.rotate_clockwise(self.cube[5])
                self.rotate_clockwise(self.cube[4])
        return self.cube

    def vertical_counterclockwise_spin(self, vcc):
        # Вращение куба против часовой стрелки ↓
        for _ in range(vcc):
            self.vertical_clockwise_spin(3)
        return self.cube

    def R_clockwise_rotation(self, Rc):
        # Вращение правой стороны по часовой стрелке
        for _ in range(Rc):
            self.rotate_clockwise(self.cube[3])
            self.cube[0][0][2], self.cube[0][1][2], self.cube[0][2][2], \
                self.cube[1][0][2], self.cube[1][1][2], self.cube[1][2][2], \
                self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0], \
                self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2] \
                = \
                self.cube[1][0][2], self.cube[1][1][2], self.cube[1][2][2], \
                self.cube[5][0][2], self.cube[5][1][2], self.cube[5][2][2], \
                self.cube[0][2][2], self.cube[0][1][2], self.cube[0][0][2], \
                self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0]
        return self.cube

    def R_counterclockwise_rotation(self, Rcc):
        # Вращение правой стороны против часовой стрелки
        for _ in range(Rcc):
            self.R_clockwise_rotation(3)
        return self.cube

    def L_clockwise_rotation(self, Lc):
        # Вращение левой стороны по часовой стрелке
        for _ in range(Lc):
            self.rotate_clockwise(self.cube[2])
            self.cube[0][0][0], self.cube[0][1][0], self.cube[0][2][0], \
                self.cube[1][0][0], self.cube[1][1][0], self.cube[1][2][0], \
                self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2], \
                self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0] \
                = \
                self.cube[4][2][2], self.cube[4][1][2], self.cube[4][0][2], \
                self.cube[0][0][0], self.cube[0][1][0], self.cube[0][2][0], \
                self.cube[5][2][0], self.cube[5][1][0], self.cube[5][0][0], \
                self.cube[1][0][0], self.cube[1][1][0], self.cube[1][2][0]
        return self.cube

    def L_counterclockwise_rotation(self, Lcc):
        # Вращение левой стороны против часовой стрелки
        for _ in range(Lcc):
            self.L_clockwise_rotation(3)
        return self.cube

    def B_clockwise_rotation(self, Bc):
        # Вращение задней стороны по часовой стрелке
        for _ in range(Bc):
            self.rotate_clockwise(self.cube[4])
            self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2], \
                self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0], \
                self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2], \
                self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2] \
                = \
                self.cube[3][2][2], self.cube[3][1][2], self.cube[3][0][2], \
                self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2], \
                self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2], \
                self.cube[2][2][0], self.cube[2][1][0], self.cube[2][0][0]
        return self.cube

    def B_counterclockwise_rotation(self, Bcc):
        # Вращение задней стороны против часовой стрелки
        for _ in range(Bcc):
            self.B_clockwise_rotation(3)
        return self.cube

    def F_clockwise_rotation(self, Fc):
        # Вращение передней стороны по часовой стрелке
        for _ in range(Fc):
            self.rotate_clockwise(self.cube[1])
            self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2], \
                self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2], \
                self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0], \
                self.cube[5][2][0], self.cube[5][2][1], self.cube[5][2][2] \
                = \
                self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2], \
                self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0], \
                self.cube[0][0][2], self.cube[0][0][1], self.cube[0][0][0], \
                self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0]
        return self.cube

    def F_counterclockwise_rotation(self, Fcc):
        # Вращение передней стороны против часовой стрелки
        for _ in range(Fcc):
            self.F_clockwise_rotation(3)
        return self.cube

    def U_clockwise_rotation(self, Uc):
        # Вращение верхней стороны по часовой стрелке
        for _ in range(Uc):
            self.rotate_clockwise(self.cube[0])
            self.cube[1][2], \
                self.cube[2][2], \
                self.cube[3][2], \
                self.cube[4][2] \
                = \
                self.cube[3][2], \
                self.cube[1][2], \
                self.cube[4][2], \
                self.cube[2][2]
        return self.cube

    def U_counterclockwise_rotation(self, Ucc):
        # Вращение верхней стороны против часовой стрелки
        for _ in range(Ucc):
            self.U_clockwise_rotation(3)
        return self.cube

    def D_clockwise_rotation(self, Dc):
        # Вращение нижней стороны по часовой стрелке
        for _ in range(Dc):
            self.rotate_clockwise(self.cube[5])
            self.cube[1][0], \
                self.cube[2][0], \
                self.cube[3][0], \
                self.cube[4][0] \
                = \
                self.cube[2][0], \
                self.cube[4][0], \
                self.cube[1][0], \
                self.cube[3][0]
        return self.cube

    def D_counterclockwise_rotation(self, Dcc):
        # Вращение нижней стороны против часовой стрелки
        for _ in range(Dcc):
            self.D_clockwise_rotation(3)
        return self.cube

    def print_cube(self):
        # Вывод развертки куба
        print('               ', self.cube[0][2])
        print('               ', self.cube[0][1])
        print('               ', self.cube[0][0])
        print(self.cube[2][2], self.cube[1][2], self.cube[3][2], self.cube[4][2])
        print(self.cube[2][1], self.cube[1][1], self.cube[3][1], self.cube[4][1])
        print(self.cube[2][0], self.cube[1][0], self.cube[3][0], self.cube[4][0])
        print('               ', self.cube[5][2])
        print('               ', self.cube[5][1])
        print('               ', self.cube[5][0])
        print()


# Использование:
cube = RubiksCube()
cube.distribute_colors(list(input('Enter your scramble -> ')))
cube.R_counterclockwise_rotation(1)
cube.L_clockwise_rotation(1)
cube.U_clockwise_rotation(1)
cube.D_counterclockwise_rotation(1)
cube.vertical_clockwise_spin(1)
cube.U_clockwise_rotation(1)
cube.D_counterclockwise_rotation(1)
cube.R_counterclockwise_rotation(1)
cube.L_clockwise_rotation(1)

cube.print_cube()
