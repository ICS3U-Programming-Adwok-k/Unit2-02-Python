#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: Feb 28th, 2025
# This program is requesting the radius
# of a circle in cm. It then calculates and
# displays the circumference using tau.
import constants


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (cm):"))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("circumference = {} cm".format(circumference))

    if __name__ == "__main__":
        main()
