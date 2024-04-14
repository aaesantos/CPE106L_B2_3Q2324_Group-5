'''
***********LABORATORY 1 - POST LAB - PROGRAMMING PROBLEM 2  ***********
CPE106L B2 Group 5

Members:
Claros, Angelica
Facal, Ma. Catherina
Santos, Angelica Anne

'''


filename = input('Enter file name: ')
number_of_lines = []
with open(filename, 'r') as f:
    for line in f:
        number_of_lines.append(line.strip())
    print("The file has", len(number_of_lines), "lines.")
    while True:
        if len(number_of_lines) == 0:
            break
        lineNumber = int(input("Enter a line number [0 to quit]: "))
        if lineNumber == 0:
            break
        elif lineNumber > len(number_of_lines):
            print("ERROR: line number must be less than or equal to", len(number_of_lines))
        else:
            print(lineNumber, ": ", number_of_lines[lineNumber - 1], "\n")
