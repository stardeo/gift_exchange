from project import *
from project import Exchange

# Valid Exchange List
a = [
    {"name": "A", "nomatch": ""},
    {"name": "B", "nomatch": ""},
    {"name": "Y", "nomatch": ""},
    {"name": "Z", "nomatch": ""},
    ]

# Valid Exchange List
b = [
    {"name": "A", "nomatch": "B"},
    {"name": "B", "nomatch": "A"},
    {"name": "C", "nomatch": "D"},
    {"name": "D", "nomatch": "C"},
    {"name": "W", "nomatch": "X"},
    {"name": "X", "nomatch": "W"},
    {"name": "Y", "nomatch": "Z"},
    {"name": "Z", "nomatch": "Y"},
    ]


# Valid Exchange List
c = [
    {"name": "A", "nomatch": "B"},
    {"name": "B", "nomatch": "A"},
    {"name": "C", "nomatch": "D"},
    {"name": "D", "nomatch": "C"},

    {"name": "E", "nomatch": ""},
    {"name": "F", "nomatch": ""},
    {"name": "G", "nomatch": ""},
    {"name": "H", "nomatch": ""},

    {"name": "I", "nomatch": "J"},
    {"name": "J", "nomatch": "K"},
    {"name": "K", "nomatch": "L"},
    {"name": "L", "nomatch": "I"},

    {"name": "M", "nomatch": ""},
    {"name": "N", "nomatch": ""},
    {"name": "O", "nomatch": ""},
    {"name": "P", "nomatch": ""},

    {"name": "Q", "nomatch": "Q"},
    {"name": "R", "nomatch": "Q"},
    {"name": "S", "nomatch": "Q"},
    {"name": "T", "nomatch": "Q"},

    {"name": "U", "nomatch": ""},
    {"name": "V", "nomatch": ""},
    {"name": "W", "nomatch": ""},
    {"name": "X", "nomatch": ""},
    ]

# Invalid Exchange
d = [
    {"name": "A", "nomatch": "D"},
    {"name": "B", "nomatch": "D"},
    {"name": "C", "nomatch": "D"},
    {"name": "D", "nomatch": ""},
    ]

# Edges

e = [
    {"name": "Alpha Bravo", "nomatch": "GOLF VON HOTEL"},
    {"name": "Charlie Delta", "nomatch": "ECHO FOXTROT"},
    {"name": "Echo Foxtrot", "nomatch": "GOLF VON HOTEL"},
    {"name": "Golf von Hotel", "nomatch": "ALPHA BRAVO"},
    ]



# Ye Olde Column Length String Measuring Comment
#12345678901234567890123456789012345678901234567890123456789012345678901234567890

# populate_exchange_list(exchange_list):
# returns True if a exchange list was generated or False if the list is empty
def test_populate_exchange_list():
    assert populate_exchange_list(a) == True
    assert populate_exchange_list(b) == True
    assert populate_exchange_list(c) == True
    assert populate_exchange_list(d) == True
    assert populate_exchange_list(e) == True


# make_matching_array(exchange_list):
# returns True if a matching array can be made successfully and False if any column
# or row adds up to 0 indicating a participant that cannot be matched with a gifter
def test_make_matching_array():
    assert make_matching_array(a) == True
    assert make_matching_array(b) == True
    assert make_matching_array(c) == True
    assert make_matching_array(d) == False
    assert make_matching_array(e) == True

exchange = Exchange()
exchange.exchange_list = [
                         {"name": "Cat", "nomatch": ""},
                         {"name": "Dog", "nomatch": ""},
                         {"name": "Bird", "nomatch": ""},
                         {"name": "Mouse", "nomatch": ""},
                         ]
exchange.random_list = [3, 2, 1, 0]

# output_exchange(exchange.random_list)
# returns the string that gets output as a side-effect.
def test_output_exchange():

    assert output_exchange(exchange.random_list, exchange.exchange_list) == "+-+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+\nCAT gives a gift to\nDOG gives a gift to\nBIRD gives a gift to\nMOUSE gives a gift to\nCAT\n+-+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+---------+-+-+-+"
