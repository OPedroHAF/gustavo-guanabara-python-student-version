import math
opposite = float(input('Type the length of the opposite side of a right triangle(cm): '))
adjacente = float(input('Type the length of the adjacente side of a right triangle(cm): '))
hypotenuse = math.sqrt(math.pow(opposite,2) + math.pow(adjacente, 2))

print('Opposite: {}\nAdjacente: {}\nHypotenuse: {}'.format(opposite,adjacente,hypotenuse))