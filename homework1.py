# -*- coding: utf-8 -*-
"""
Muhammad Mashwani
PeopleSoft ID: 1378052
COSC 1306 
Homework #1
"""
GALLON = 400 #one gallon covers 400 square feet
TILES = 9 # amount of 4" x 4" tiles needed to cover one square foot 

def get_value(parameter):
    return int(input("Please enter the " + parameter + " of the room in feet: "))

def round_up(number):
    return int(number + 0.99) #To Do Fix this to actually work 

length = get_value("length")  
width = get_value("width")
height = get_value("height")

area_of_walls_1 = length * height
area_of_walls_2 = width * height
area_of_ceiling = length * width

total_area = ((2*area_of_walls_1) + (2*area_of_walls_2) + area_of_ceiling)

gallons_needed = round_up(total_area / GALLON)

area_of_floor = area_of_ceiling 

tiles_needed = area_of_floor * TILES

print()
print("The total paint needed to cover the walls and ceiling is " + str(gallons_needed) + " gallons.")
print()
print("The total number of tiles to cover the floor is " + str(tiles_needed) + ".")