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


# define, how a dice can look like and how its calculated
class Dice:
    """ At every position, a dice is placed """
    def __init__(self, side, calc, fact):
        if side in range(1, 7):
            self.side = side
        else:
            print("Ungültiger Würfel")

        if calc in range(0, 4):
            self.calc = calc
        else:
            print("Ungültige Berechnung")

        if fact is True:
            self.fact = True
            self.side = math.factorial(self.side)
        else:
            self.fact = False


    def __str__(self):
        if self.fact is False:
            return str(self.side)
        return str(self.side) + "!"

    def get_fact(self):
        """ returns factorial of the dice """
        return math.factorial(self.side)

# define, what a result looks like
class Combination:
    """ a Combination consists of up to 4 dices and a result """
    def __init__(self):
        dices = []
        self.dices = dices
        order = []
        self.order = order
        calc_string = ""
        self.calc_string = calc_string
        self.result = 0
        self.calc_rule = 0

    def __str__(self):
        return self.calc_string

    def get_result(self):
        """ Calculates result and creates result string """
        self.result = 0
        self.calc_rule = 4
        for position in self.dices:

            # if brackets have to be written,
            # we insert them here in the string according to math rules
            if position.calc > self.calc_rule:
                # logging.debug(position.calc)
                # logging.debug(self.calc_rule)
                self.calc_string = "(" + self.calc_string + ")"
                # logging.debug(self.calc_string)

            if position.calc == 0:
                self.result = self.result + position.side
                if self.calc_string == "":
                    self.calc_string = str(position.side)
                else:
                    self.calc_string = self.calc_string + "+" + str(position.side)
                    self.calc_rule = 1
            elif position.calc == 1:
                self.result = self.result - position.side
                self.calc_string = self.calc_string + "-" + str(position.side)
                self.calc_rule = 1
            elif position.calc == 2:
                self.result = self.result * position.side
                self.calc_string = self.calc_string + "*" + str(position.side)
                self.calc_rule = 3
            elif position.calc == 3:
                self.result = self.result / position.side
                self.calc_string = self.calc_string + "/" + str(position.side)
                self.calc_rule = 3
            elif position.calc == 4:
                self.result = self.result ** position.side
                self.calc_string = self.calc_string + "**" + str(position.side)
                self.calc_rule = 4
            else:
                print("Error")

        # logging.debug(self.result)

        return self.result, self.calc_string

    def add_dice(self, dice):
        """ add a dice to the Combination """
        if len(self.dices) < 4:
            self.dices.append(dice)
        else:
            print("max. 4 Würfel pro Kombination!")


def all_combinations(number1, number2, result):
    """
    Defines a set of all possible outcomes that lead to the result
    The result is a string in the format of "(1+1)*3*3"
    """

    # each number can also be used as factorial,
    # that gives up to four possible numbers for each position
    # TODO: not math.factorial integrated yet
    # TODO: 3 and 4 numbers

    number_set = set()
    number_set.update([number1, number2])
    result_set = set()
    logging.debug("%s, %s", number1, number2)

    for pos1 in number_set:
        if pos1 is result:
            result_set.add(pos1)
            logging.debug("%s ergibt %s", pos1, pos1)
        for pos2 in number_set:
            logging.debug("%s, %s", pos1, pos1)
            for calc_type in range(0, 4):
                kombination = Combination()
                kombination.add_dice(Dice(pos1, 0, False))
                kombination.add_dice(Dice(pos2, calc_type, False))
                kombination_erg = kombination.get_result()
                # logging.debug("%s ergibt %s", kombination_erg[1], kombination_erg[0])
                if kombination_erg[0] is result:
                    result_set.add(kombination_erg[1])
                    logging.debug("%s ergibt %s", kombination_erg[1], kombination_erg[0])
    return result_set


def main():
    """
    Solves number puzzles in the style of  Heinz Böer:
        x ? y = z
    While x and y are dice results between 1 and 6
    Each dice can be used 0, 1 or 2 times in the calculation
    Allowed are +, -, *, /, Power and Factorials
    """

    # Test all combinations
    print(all_combinations(1, 2, 2))

    # Test Class Combination:
    neue_kombi = Combination()
    neue_kombi.add_dice(Dice(6, 0, False))
    neue_kombi.add_dice(Dice(6, 2, False))
    neue_kombi.add_dice(Dice(2, 1, False))
    neue_kombi.add_dice(Dice(2, 3, False))
    print(neue_kombi.get_result()[1] + "=" + str(neue_kombi.get_result()[0]))

main()
