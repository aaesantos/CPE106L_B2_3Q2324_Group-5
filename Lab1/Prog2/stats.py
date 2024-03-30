'''
**********LABORATORY 1 - POST LAB - PROGRAMMING PROBLEM 1  **********
CPE106L B2 Group 5

Members:
Claros, Angelica
Facal, Ma. Catherina
Santos, Angelica Anne

'''

import statistics

def Average(self):
    return statistics.mean(self)

def Median(self):
    return statistics.median(self)

def Mode(self):
    return statistics.mode(self)

print("List of numbers: 3, 82, 57, 95, 72, 68, 84, 59, 76, 91")

scores=[63, 82, 57, 95, 72, 68, 84, 59, 76, 91]

print("Average: ",Average(scores))
print("Median: ", Median(scores))
print("Mode: ", Mode(scores))

