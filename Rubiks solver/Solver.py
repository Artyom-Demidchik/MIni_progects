import Cube

# byyyworrwyybwgbworoobroggborbbrrwggooryobyggwgwybywrgw
# wwwwwwwwwgggggggggooooooooorrrrrrrrrbbbbbbbbbyyyyyyyyy

cube = Cube.RubiksCube()
cube.distribute_colors(list(input('Enter your scramble -> ')))


cube.print_cube()

