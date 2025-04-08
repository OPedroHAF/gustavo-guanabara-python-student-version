from math import sin, cos, tan, radians, degrees

# Get input angle in degrees and convert it to radians
angle_degrees = float(input('Type an angle: '))
angle_radians = radians(angle_degrees)

# Calculate sine, cosine, and tangent in radians
sine = sin(angle_radians)
cosine = cos(angle_radians)
tangent = tan(angle_radians)

# Handle precision issues with cosine (near zero values)
if abs(cosine) < 1e-15:
    cosine = 0
if abs(sine) < 1e-15:
    sine = 0

# Handle large tangent values (approaching infinity)
if abs(tangent) > 1e+15:
    tangent = float('inf')
elif abs(tangent) < 1e-15:
    tangent = 0
# Print the results
print('Angle: {}°\nSine: {}\nCosine: {}\nTangent: {}'.format(angle_degrees, sine, cosine, tangent))
