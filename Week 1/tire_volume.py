import math
from datetime import datetime

# v = (math.pi() * w**2 *(w * a + 2540 * d)) / 10000000000
# "v" = Volume in Liters
# "math.pi" = 3.1415.....
# "w" is the width of the tire in millimeters
# "a" = aspect ratio of the tire
# "d" = is the diameter of the wheel 
def calculate_voume_of_space(w,a,d,):
    v = (math.pi * (w**2) * a * (w * a + 2540 * d)) / 10000000000
    return v

time = datetime.now(tz=None)


width_in_milimeters = int(input('What is the width in milimeters?: '))

aspect_ratio = int(input('What is the aspect ratio?: '))

diameter_of_wheel = int(input('What is the diameter of the wheel in inches?: '))


volume_in_liters = calculate_voume_of_space(width_in_milimeters,aspect_ratio, diameter_of_wheel)

print(f'The aproximate volume is {volume_in_liters:.2f} liters')

#opens and writes variables to volumes.txt
with open("volumes.txt", "at") as volumes_file:

    print(f'{time:%y-%m-%d}, {width_in_milimeters}, {aspect_ratio}, {diameter_of_wheel}, {volume_in_liters:.2f}', file=volumes_file)