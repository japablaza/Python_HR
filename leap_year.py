#!/usr/bin/python3

# This is the function we can use  later
# Link
# https://www.hackerrank.com/challenges/write-a-function/problem

year = int(input("Give me a year: "))


def is_leap(year):
    leap = False
    if year % 4 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 400 == 0:
        return True
    else:
        return leap


print(is_leap(year))
