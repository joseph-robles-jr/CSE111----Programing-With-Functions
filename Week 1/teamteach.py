"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""
import math

def equation(length):
	f = math.pi * 2
	inside = length / 9.81
	square_root = math.sqrt(inside)
	final = f * square_root
	return final

length = float(input("Please input the length of the pendulim in meters: "))

time = equation(length)

print(f"{time:.2f}")