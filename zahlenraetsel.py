#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
Copyright (c) 2020 Achim Barczok (achim@barczok.de)
All rights reserved.

Solves number puzzles in the style of Heinz Böer

"""

import math
import logging

# some debug options
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


# define, how a dice can look like
class Dice:
    def __init__(self, side, fact):
        if (side) in range(1, 6):
            self.side = side
        else:
            print("Ungültiger Würfel")
        if (fact) is True:
            self.fact = True
        else:
            self.fact = False

    def get_side(self):
        return self.side

    def get_fact(self):
        return math.factorial(self.side)


# define, what a result looks like
class Combination:
    def __init__(self):
        dices = []
        self.dices = dices

        result

    def __str__(self):
        calc_string = ""
        self.calc_string = calc_string

    def add_dice(self, dice):
        self.dices.append(dice)


def computing(number1, number2, operator):
    """
    Computes two numbers:
    Addition, Subtraction, Multiplication, Division, Power
    """

    if operator == 0:
        return number1 + number2
    if operator == 1:
        return number1 - number2
    if operator == 2:
        return number1 / number2
    if operator == 3:
        return number1 * number2
    if operator == 4 and number2 < 10000 and number1 < 100:
        # as computing high numbers with Powers take very long and
        # and are unlikely to give good results, we strip them a bit
        return number1 ** number2

    # returns 0 if no or wrong operator is given
    return 0


def all_combinations(number1, number2, result):
    """
    Defines a set of all possible outcomes that lead to the result
    The result is a string in the format of "(1+1)*3*3"
    """

    # each number can also be used as factorial,
    # that gives up to four possible numbers for each position
    number_set = set()
    number_set.update([number1, number2, math.factorial(number1), math.factorial(number2)])

    for pos1 in number_set:
        logging.debug(pos1)
        if pos1 is result:
            logging.debug(str(pos1) + " ergibt " + str(result))
        for pos2 in number_set:
            logging.debug(str(pos1) + ", " + str(pos2))

    # TODO: generate string for the result

    # TODO: add 2nd position

    # TODO: add 3rd position

    # TODO: add 4th position
    return ()


def main():
    """
    Solves number puzzles in the style of  Heinz Böer:
        x ? y = z
    While x and y are dice results between 1 and 6
    Each dice can be used 0, 1 or 2 times in the calculation
    Allowed are +, -, *, /, Power and Factorials
    """

    all_combinations(1, 2, 2)


main()
