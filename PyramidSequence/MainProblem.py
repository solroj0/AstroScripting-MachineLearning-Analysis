"""
This program solves a challenge. There is a file in this directory organized with random #'s 
and corresponding words. The pattern uses a sequence I have decoded below.
The result is printed onto the terminal.

"""

import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "coding_qual_input.txt")



data = [] 

#first I am opening the file and reading each line as two variables seperated by a space
#every line is appended as a pair into the tuple 'data'
with open(file_path, "r") as file:
    for line in file:
        x, y = line.strip().split(' ', 1)
        data.append((int(x), y))


# Sort the 'data' list of tuples based on the first element 'x' of each tuple and store it in 'sorted_data'
sorted_data = sorted(data, key=lambda x: x[0])

# Calculate the number of tuples in the 'sorted_data' list and store it in 'size'
size = len(sorted_data)

message = ""
n, nsum = 1, 2 

# Iterate through the sorted data and append the 'y' value of each tuple to 'message'
while n < size:
    index = n - 1
    message += sorted_data[index][1] + " "
    n, nsum = n + nsum, nsum + 1

print(message)
