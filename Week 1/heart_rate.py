"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""


age = int(input("What is your age?"))

max_heart_rate = 220 - age

max_excercise_rate = max_heart_rate * .85
min_excercise_rate = max_heart_rate * .65

print(f"your ideal excercise heart rate is between {min_excercise_rate:.0f} and {max_heart_rate:.0f} bpm.")
