#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: May 2022
# This program calculates the LCM of two integers
#   that are user inputted

import math


def main():
    # this creates the lcm program

    # input

    integer1 = input("Enter first number: ")
    integer2 = input("\nEnter second number: ")

    # process & output

    try:
        integer1_int = int(integer1)
        integer2_int = int(integer2)

        if integer1_int > integer2_int:
            greater = integer1_int
        else:
            greater = integer2_int
        while True:
            if (greater % integer1_int == 0) and (greater % integer2_int == 0):
                lcm = greater
                break
            greater += 1
        print("\nThe L.C.M. of", integer1, "and", integer2, "is", lcm)

    except Exception:
        print("\nPlease input two valid integers.")


if __name__ == "__main__":
    main()
