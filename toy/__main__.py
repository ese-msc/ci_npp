import sys

from . import Rectangle


if len(sys.argv) < 3:
    print('Usage: python -m toy <length> <width>')
    sys.exit(1)

width = int(sys.argv[1])
height = int(sys.argv[2])


rectangle = Rectangle(width, height)
print(f'Area is: {rectangle.area()}')


