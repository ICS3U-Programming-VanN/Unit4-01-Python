#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: October 26, 2022
# This program asks the user for a positive number and
# uses a while loop to add up all the whole numbers starting from 0
# It will then display the sum to the user


def main():
    # Initialize Variables
    loop_counter = 0
    number_sum = 0

    # Asks user to enter a number
    user_number_string = input("Enter a positive integer: ")

    # Checks for exceptions
    try:

        # Attempts to cast user_number_string to integer
        user_number = int(user_number_string)

    # In the event of an exception
    except Exception:
        print(f"{user_number_string} is not a WHOLE positive integer!")

    # In the event of no exceptions
    else:

        # If the user enters a negative number
        if user_number < 0:
            print(f"{user_number} is not a POSITIVE integer!")

        # If the user entered a positive number
        else:

            # Calculates the total sum and displays how many times it has looped
            while loop_counter <= user_number:

                # Displays how many times it has gone through the loop
                print(f"Tracking {loop_counter} times through the loop.")

                # Calculates the sum of all the numbers added up (from user's number)
                number_sum += loop_counter

                # Increments loop_counter
                loop_counter += 1

            # Displays sum to user
            print(f"The sum of the numbers from 0 to {user_number} = {number_sum}")


if __name__ == "__main__":
    main()
