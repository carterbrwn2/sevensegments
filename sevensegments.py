# Author: Carter Brown

# Takes "Clock" Numbers from input and outputs them as an integer string

numbers = [[" _ | ||_|", 0],
       ["     |  |", 1],
       [" _  _||_ ", 2],
       [" _  _| _|", 3],
       ["   |_|  |", 4],
       [" _ |_  _|", 5],
       [" _ |_ |_|", 6],
       [" _   |  |", 7],
       [" _ |_||_|", 8],
       [" _ |_| _|", 9]]

# Get input

line1 = input()
line2 = input()
line3 = input()

raw_input = [[line1[i:i+3] for i in range(0, len(line1), 3)],
         [line2[i:i + 3] for i in range(0, len(line2), 3)],
         [line3[i:i + 3] for i in range(0, len(line3), 3)]]

# Formatted input in same style as "numbers"

f_input = ["" for i in range(int(len(line1)/3))]

i = 0
while i < len(line1)/3:
    j = 0
    num_string = ""
    while j < 3:
        num_string += raw_input[j][i]
        j += 1
    f_input[i] = num_string
    i += 1

# Print numbers based on input

for cl_input in f_input:
    for num in numbers:
        if cl_input == num[0]:
            print(num[1], end="")
