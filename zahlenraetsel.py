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
    """ At every position, a dice is placed """
    def __init__(self, side, fact):
        if side in range(1, 6):
            self.side = side
        else:
            print("Ungültiger Würfel")
        if fact is True:
            self.fact = True
        else:
            self.fact = False

    def __str__(self):
        return str(self.side)

    def get_side(self):
        """ returns side of the dice """
        return self.side

    def get_fact(self):
        """ returns factorial of the dice """
        return math.factorial(self.side)

class Calculation:
    """ Between each dice pair, a calculation can be made """
    def __init__(self, type, order):
        if type in range(1, 4):
            self.type = type
        else:
            print("ungültige Berechnung")
        if order is True:
            self.order = order
        else:
            self.order = 0

    def __str__(self):
        if self.type == 0:
            return "+"
        if self.type == 1:
            return "-"
        if self.type == 2:
            return "*"
        if self.txpe == 3:
            return "/"
        if self.type == 4:
            return "*"


# define, what a result looks like
class Combination:
    """ a Combination consists of up to 4 dices and a result """
    def __init__(self):
        dices = []
        self.dices = dices
        calculations = []
        self.calculations = calculations
        order = []
        self.order = order
        calc_string = ""
        self.calc_string = calc_string

    def __str__(self):
        return self.calc_string

    def get_result(self):
        self.result = 0
        for pos1 in self.dices:
            self.result = self.result + pos1
            self.calc_string = self.calc_string + str(pos1)
        return self.result

    def add_dice(self, dice):
        """ add a dice to the Combination """
        if len(self.dices) < 5:
            self.dices.append(dice)
        else:
            print("max. 4 Würfel pro Kombination!")

    def add_calc(self, calc):
        """ add a calculation to the Combinaction """
        if len(self.calculations) < 3:
            self.calculations.append(calc)
        else:
            print("max. 3 Berechnungen!")


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
            logging.debug("%s ergibt %s", pos1, pos2)
        for pos2 in number_set:
            logging.debug("%s, %s", pos1, pos2)

    return ()


def main():
    """
    Solves number puzzles in the style of  Heinz Böer:
        x ? y = z
    While x and y are dice results between 1 and 6
    Each dice can be used 0, 1 or 2 times in the calculation
    Allowed are +, -, *, /, Power and Factorials
    """

    # all_combinations(1, 2, 2)

    # mit Klassen testen:
    neue_kombi = Combination()
    neue_kombi.add_dice(6)
    neue_kombi.add_calc(2)
    neue_kombi.add_dice(1)
    neue_kombi.add_calc(2)
    neue_kombi.add_dice(1)
    neue_kombi.add_calc(2)
    neue_kombi.add_dice(1)
    print(neue_kombi.get_result())


main()
