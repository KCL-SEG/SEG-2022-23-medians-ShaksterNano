"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        size = len(numbers)
        if size % 2 == 0:
            median = (numbers[size // 2] + numbers[size // 2 - 1]) / 2
        else:
            median = numbers[size // 2]
        print(median)
    except ValueError:
        print("Some input could not be converted to a number!")
