widthMeters = float(input('Width of the wall: '))
heightMeters = float(input('Height of the wall: '))
squareArea = widthMeters * heightMeters
litersPaint = squareArea / 2

print('To paint {}m² it would require {}L of paint'.format(squareArea, litersPaint))
