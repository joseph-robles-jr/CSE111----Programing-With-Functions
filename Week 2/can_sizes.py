'''In many countries, food is stored in steel cans 
(also known as tin cans) that are shaped like cylinders. 
There are many different sizes of steel cans. The storage efficiency of a can 
tells us how much a can stores versus how much steel is required to make the can. 
Some sizes of cans require a lot of steel to store a small amount of food. 
Other sizes of cans require less steel and store more food. 
A can size with a large storage efficiency is considered more friendly 
to the environment than a can size with a small storage efficiency.'''



import math

#R 6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10 
#H 10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11
#C 0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42

# Needs volume and surface
def storage_efficiency(volume, surface_area):
  '''Calculates storage efficiency by dividing volume by surface_area'''
  return volume / surface_area

# Needs radius and height
def volume(radius, height):
  '''Calculates the volume by pi*r^2*h'''
  return math.pi * (radius**2) * height

# Needs radius and height
def surface_area(radius, height):
  '''Calculates the Surface Area'''
  return 2 * math.pi * radius *(radius + height)
  

def main():
  max = -99999999999999999999999
  min = 99999999999999999999999999
  max_name = ''
  max_cost = 0.00
  
  
  with open('can_sizes.csv') as can_sizes:
    can_sizes.readline()
    for line in can_sizes:
        line_strip = line.strip()
        line_data = line_strip.split(',')


        name = line_data[0]
        radius = float(line_data[1])
        height = float(line_data[2])
        cost = float(line_data[3])

        volume_can = volume(radius, height)
        surf_area = surface_area(radius,height)
        storage = storage_efficiency(volume_can, surf_area)

        #finds maximim storage efficiency
        if storage > max:
          max = storage
          max_name = name
          max_cost = cost

        #Finds minimum sstorage efficiency
        if storage < min:
          min = storage
          min_name = name
          min_cost = cost
          
    print(f'The most efficient can is {max_name} with a efficency of {max:.2f} at ${max_cost}') 
main() 