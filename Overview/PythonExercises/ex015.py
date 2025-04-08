from math import sin, cos, tan, radians, degrees
angle = radians(float(input('Type an angle: ')))
sine = sin(angle)
cosine = cos(angle)
tangent = tan(angle)

if abs(sine) < 1e-15:
    sine = 0
if abs(cosine) < 1e-15:
    cosine = 0
if abs(tangent) > 1e+15:
    tangent = float('inf')
elif abs(tangent) < 1e-15:
    tangent = 0

print('Angle: {}\nSine: {}\nCosine: {}\nTangent: {}'.format(degrees(angle), sine, cosine, tangent))