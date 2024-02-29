import math

# This example demonstrates using methods and using functions that YOU define to calculate 
# how many boxes would be neede if you have a given number of items and want a certain number per box.


# Finds the number of boxes you need for a given number of items and a itemps per box number
def get_boxes_needed(items_per_box, total_items):
    number_of_boxes = total_items / items_per_box
    return math.ceil(number_of_boxes)

total_items = int(input('Enter the number of items: '))
item_per_box = int(input('How many items will be in each box?: '))

boxes_needed = (get_boxes_needed(item_per_box, total_items))

print(f'Total number of boxes needed is: {boxes_needed} boxes')    