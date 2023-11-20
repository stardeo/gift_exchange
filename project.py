###  _______  _______  _______  _______  _______  ___
### |       ||       ||       ||  _    ||       ||   |
### |       ||  _____||   ____|| | |   ||    _  ||___|
### |       || |_____ |  |____ | | |   ||   |_| | ___
### |      _||_____  ||_____  || |_|   ||    ___||   |
### |     |_  _____| | _____| ||       ||   |    |___|
### |_______||_______||_______||_______||___|
### 
###  _______  ___   _______  _______    _______  __   __  _______  __   __  _______  __    _  _______  _______
### |       ||   | |       ||       |  |       ||  |_|  ||       ||  | |  ||   _   ||  |  | ||       ||       |
### |    ___||   | |    ___||_     _|  |    ___||       ||       ||  |_|  ||  |_|  ||   |_| ||    ___||    ___|
### |   | __ |   | |   |___   |   |    |   |___ |       ||       ||       ||       ||       ||   | __ |   |___
### |   ||  ||   | |    ___|  |   |    |    ___| |     | |      _||       ||       ||  _    ||   ||  ||    ___|
### |   |_| ||   | |   |      |   |    |   |___ |   _   ||     |_ |   _   ||   _   || | |   ||   |_| ||   |___
### |_______||___| |___|      |___|    |_______||__| |__||_______||__| |__||__| |__||_|  |__||_______||_______|
### By
###  ______   _______  __    _  ___   _______  ___        __   __  _______  ______   _______  __   __  __   __  _______  __   __  __   __
### |      | |   _   ||  |  | ||   | |       ||   |      |  | |  ||       ||      | |   _   ||  |_|  ||  | |  ||       ||  | |  ||  | |  |
### |  _    ||  |_|  ||   |_| ||   | |    ___||   |      |  |_|  ||    ___||  _    ||  |_|  ||       ||  | |  ||_     _||  |_|  ||  | |  |
### | | |   ||       ||       ||   | |   |___ |   |      |       ||   |___ | | |   ||       ||       ||  |_|  |  |   |  |       ||  |_|  |
### | |_|   ||       ||  _    ||   | |    ___||   |___   |       ||    ___|| |_|   ||       ||       ||       |  |   |  |       ||       |
### |       ||   _   || | |   ||   | |   |___ |       |   |     | |   |___ |       ||   _   || ||_|| ||       |  |   |  |   _   ||       |
### |______| |__| |__||_|  |__||___| |_______||_______|    |___|  |_______||______| |__| |__||_|   |_||_______|  |___|  |__| |__||_______|
### From
### ______    _______  _______  __   __  _______  _______  _______  _______  ______      __   __  __    _    __   __  _______  _______
### |    _ |  |       ||       ||  | |  ||       ||       ||       ||       ||    _ |    |  |_|  ||  |  | |  |  | |  ||       ||   _   |
### |   | ||  |   _   ||       ||  |_|  ||    ___||  _____||_     _||    ___||   | ||    |       ||   |_| |  |  | |  ||  _____||  |_|  |
### |   |_||_ |  | |  ||       ||       ||   |___ | |_____   |   |  |   |___ |   |_||_   |       ||       |  |  |_|  || |_____ |       |
### |    __  ||  |_|  ||      _||       ||    ___||_____  |  |   |  |    ___||    __  |  |       ||  _    |  |       ||_____  ||       |
### |   |  | ||       ||     |_ |   _   ||   |___  _____| |  |   |  |   |___ |   |  | |  | ||_|| || | |   |  |       | _____| ||   _   |
### |___|  |_||_______||_______||__| |__||_______||_______|  |___|  |_______||___|  |_|  |_|   |_||_|  |__|  |_______||_______||__| |__|


### With thanks to Seth Black for his documentation of his pyge module to help me understand I should create a "truth table" two array!
### https://www.sethserver.com/python/secret-santa-gift-exchange.html

import random
import re
import sys

import numpy

class Exchange:
    exchange_list = []
    random_list = []

exchange = Exchange()

def main():
    if populate_exchange_list(exchange.exchange_list) == False:
        sys.exit("Must have at least one participant in the Exchange")

    if make_matching_array(exchange.exchange_list) == False:
        print(f"\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/")
        print("Invalid Exchange.")
        print("At least one participant cannot be matched with a gifter.")
        print(f"/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\")
        sys.exit()

    while len(exchange.random_list) < len(exchange.exchange_list):
        shuffle_exchange(exchange.random_list, exchange.matching_array)

    output = output_exchange(exchange.random_list, exchange.exchange_list)
    print(output)

          # Ye Olde Column Length String Measuring Comment
          #12345678901234567890123456789012345678901234567890123456789012345678901234567890
def output_exchange(random_list, exchange_list):
    output = f"+-+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+\n"
    for participant in reversed(random_list):
        output = output + exchange_list[participant]["name"].upper() + " gives a gift to\n"
    output = output + exchange_list[random_list[-1]]["name"].upper() + "\n"
    output = output + "+-+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+"
    return output


def populate_exchange_list(exchange_list):
    if exchange_list == []:
        print("+-+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+")
        print("                  Getting names for a new exchange list                  ")
        print("+-+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+")
        print("Input participant names.                                                 ")
        print("If the participant should not give a gift to another participant input   ")
        print("that participant's name separated by a comma.                            ")
        print("     Example: Sauron                                                     ")
        print("     Example: Mario, Peach                                               ")
        print("     Example: Scott Pilgrim, Envy Adams                                  ")
        print("+-+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+")
        n = 1
        while True:
            s = input(f"Participant {n}: ").strip()
            if s == "":
                if exchange_list == []:
                    return False
                else:
                    return True
            if capture := re.split(r"\s*,\s*", s):
                n += 1
                if len(capture) == 1:
                    capture.append("")
                participant = {"name": capture[0], "nomatch": capture[1]}
                exchange.exchange_list.append(participant)
    return True




def make_matching_array(exchange_list):
    exchange.matching_array = numpy.ones((len(exchange_list),len(exchange_list)))

    for i, row in enumerate(exchange_list):  # ROWS // RECIEVERS
        for j, column in enumerate(exchange_list): # COLUMNS // GIFTERS
            if row["name"].lower() == column["nomatch"].lower():
                exchange.matching_array[i, j] = 0
            if row["name"].lower() == column["name"].lower():
                exchange.matching_array[i, j] = 0

    if 0 in exchange.matching_array.sum(axis=1): # ROWS // RECIEVERS
        return False
    elif 0 in exchange.matching_array.sum(axis=0): # COLUMNS // GIFTERS
        return False
    else:
        return True


def shuffle_exchange(random_list, matching_array):
    rows = matching_array.sum(axis=1)
    row_min = min(rows[rows > 0]) # Find the value of the ROWS with the lowest non-zero sum. (RECIEVERS)
    row_positions = []
    for i, row in enumerate(rows):
        if row == row_min:
            row_positions.append(i)

 #   PLACEHOLDER IN CASE WANT TO ADD MULTIPLE NO MATCHES LOGIC NOT YET IMPLEMENTED BELOW
 #   columns = matching_array.sum(axis=0)
 #   column_min = min(columns[columns > 0]) # Find the value of the COLUMNS with the lowest non-zero sum. (GIFTERS)
 #   column_positions = []
 #   for j, column in enumerate(columns):
 #       if column == column_min:
 #           column_positions.append(j)

    if random_list == []:
        choice_a = random.choice(row_positions)
        random_list.append(choice_a)
    else:
        choice_a = -1

    potential_matches = []
    for k, tester in enumerate(matching_array[random_list[-1], :]):
        if  tester == 1:
            potential_matches.append(k)
    choice = random.choice(potential_matches)

    if choice_a > 0:
        matching_array[choice_a, :] = 0
    exchange.matching_array[:, random_list[-1]] = 0

    exchange.random_list.append(choice)

    return True



if __name__ == "__main__":
    main()

