#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Dec 2022
# This program calculates the average

import random


def calculate_average(passed_in_2D_list, rows, columns):
    # This function calculates the average of the integers in the 2D array

    average = 0
    sum = 0

    for row_value in passed_in_2D_list:
        for single_element in row_value:
            sum += single_element
    average = sum / (rows * columns)

    return average


def main():
    # this function uses an array
    a_2d_list = []

    # input
    str_rows = input("How many row would you like: ")
    str_columns = input("How many columns would you like: ")

    # process
    try:
        rows = int(str_rows)
        columns = int(str_columns)

        for loop_counter_rows in range(0, rows):
            random_numbers = []
            for loop_counter_colums in range(0, columns):
                a_random_number = random.randint(1, 50)  # a number between 1 and 100
                random_numbers.append(a_random_number)
                print("{0} ".format(a_random_number), end="")
            a_2d_list.append(random_numbers)
            print("")

        total_average = calculate_average(a_2d_list, rows, columns)
        print("\nThe average is: {0}.".format(round(total_average, 2)))
    except ValueError:
        print("Invalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
