#!/usr/bin/python3
# Print numbers from 00 to 99
# Separated by a ', ' last number ends with newline

for n in range(0, 100):
    if n != 99:
        print("{:02}".format(n), end=", ")
    else:
        print("{:02}".format(n))
