#!/usr/bin/python3

N = int(input("Give me a number: "))

if N%2 == 1:
    print("Weird")
elif ((N%2 == 0) & (2 <= N <= 5)):
    print("Not Weird")
elif ((N%2 == 0) & (6 <= N <= 20)):
    print("Weird")
elif ((N%2 == 0) & (N > 20)):
    print("Not Weird")
