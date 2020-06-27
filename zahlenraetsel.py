#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
Solves number puzzles in the style of Heinz Böer

Copyright (c) 2020 Achim Barczok (achim@lostfile.de)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import math
import logging
import itertools
import copy


# some debug options
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


class Dice:
    """ At every position, a dice is placed """
    def __init__(self, side, calc, fact):
        if side in range(1, 7):
            self.side = side
        else:
            print("Ungültiger Würfel")

        if calc in range(0, 5):
            self.calc = calc
        else:
            print("Ungültige Berechnung")

        # define rules for brackets in strings
        if calc in range(0, 2):
            self.calc_range = 1

        if calc in range(2, 2):
            self.calc_range = 3

        if calc == 4:
            self.calc_range = 4

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
        self.calc_rule = 1
        self.dice = []
        self.pos1 = 0
        self.pos2 = 0
        self.string1 = ""
        self.string2 = ""

    def __str__(self):
        return self.calc_string

    def get_result(self):
        """ returns result and string """

        return self.result, self.calc_string

    def add_dice(self, dice, reverse=False):
        """ add a dice to the Combination """

        self.dice = dice
        if len(self.dices) < 4:
            self.dices.append(self.dice)
        else:
            print("max. 4 Würfel pro Kombination!")

        # if brackets have to be written,
        # we insert them here in the string according to math rules
        if len(self.dices) > 2 and self.dice.calc > self.calc_rule:
            self.calc_string = "(" + self.calc_string + ")"

        # if dice should be added in front of the calculation,
        # set it here
        if reverse:
            self.pos1 = self.dice.side
            self.pos2 = self.result
            self.string1 = str(self.dice.side)
            self.string2 = self.calc_string
        else:
            self.pos2 = self.dice.side
            self.pos1 = self.result
            self.string2 = str(self.dice.side)
            self.string1 = self.calc_string

        if self.dice.calc == 0:
            self.result = self.pos1 + self.pos2
            # if it's the first dice, only the dice string is put in the string
            if self.calc_string == "":
                self.calc_string = self.string2
            else:
                self.calc_string = self.string1 + "+" + self.string2
                self.calc_rule = 1
        elif self.dice.calc == 1:
            self.result = self.pos1 - self.pos2
            self.calc_string = self.string1 + "-" + self.string2
            self.calc_rule = 1
        elif self.dice.calc == 2:
            self.result = self.pos1 * self.pos2
            self.calc_string = self.string1 + "*" + self.string2
            self.calc_rule = 3
        elif self.dice.calc == 3:
            self.result = self.pos1 / self.pos2
            self.calc_string = self.string1 + "/" + self.string2
            self.calc_rule = 3
        elif self.dice.calc == 4:
            self.result = self.pos1 ** self.pos2
            self.calc_string = self.string1 + "**" + self.string2
            self.calc_rule = 4
        else:
            print("Error")





def all_combinations(number1, number2, result):
    """
    Defines a set of all possible outcomes that lead to the result
    The result is a string in the format of "(1+1)*3*3"
    """

    # each number can also be used as factorial,
    # that gives up to four possible numbers for each position
    # TODO: not math.factorial integrated yet

    number_set = set()
    number_set.update([number1, number2])
    result_set = set()

    # use itertools, to have less nested loops
    for positions in itertools.product(number_set, repeat=4):

        #only calculate, if number 1 and number 2 are used twice
        if (positions[0]+positions[1]+positions[2]+positions[3]) == (number1*2 + number2*2):

            for calc_types in itertools.product(range(0, 5), repeat=3):

                kombination = Combination()

                kombination.add_dice(Dice(positions[0], 0, False))
                kombination_erg = kombination.get_result()
                if kombination_erg[0] is result:
                    result_set.add(kombination_erg[1])

                kombination.add_dice(Dice(positions[1], calc_types[0], False))
                kombination_erg = kombination.get_result()
                if kombination_erg[0] is result:
                    result_set.add(kombination_erg[1])

                kombination2 = copy.copy(kombination)

                kombination.add_dice(Dice(positions[2], calc_types[1], False))
                kombination_erg = kombination.get_result()
                if kombination_erg[0] is result:
                    result_set.add(kombination_erg[1])

                if kombination_erg[0] != 0 and calc_types[1] != 3:
                    kombination2.add_dice(Dice(positions[2], calc_types[1], False), True)
                    kombination_erg = kombination2.get_result()
                    if kombination_erg[0] is result:
                        result_set.add(kombination_erg[1])

                kombination3 = copy.copy(kombination)
                kombination4 = copy.copy(kombination2)
                print(len(kombination3.dices))

                kombination.add_dice(Dice(positions[3], calc_types[2], False))
                kombination_erg = kombination.get_result()
                if kombination_erg[0] is result:
                    result_set.add(kombination_erg[1])

                kombination2.add_dice(Dice(positions[3], calc_types[2], False))
                kombination_erg = kombination2.get_result()
                if kombination_erg[0] is result:
                    result_set.add(kombination_erg[1])

                if kombination_erg[0] != 0 and calc_types[2] != 3:
                    kombination3.add_dice(Dice(positions[3], calc_types[2], False), True)
                    kombination_erg = kombination3.get_result()
                    if kombination_erg[0] is result:
                        result_set.add(kombination_erg[1])

                if kombination_erg[0] != 0 and calc_types[2] != 3:
                    kombination4.add_dice(Dice(positions[3], calc_types[2], False), True)
                    kombination_erg = kombination4.get_result()
                    if kombination_erg[0] is result:
                        result_set.add(kombination_erg[1])
                print

                #logging.debug("Kombi: %s", kombination_erg[1])

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
    print(len(all_combinations(1, 2, 3)))
    print(all_combinations(1, 2, 3))

    # Test Class Combination:
    neue_kombi = Combination()
    neue_kombi.add_dice(Dice(6, 0, False))
    neue_kombi.add_dice(Dice(6, 2, False))
    neue_kombi.add_dice(Dice(2, 1, False))
    neue_kombi.add_dice(Dice(2, 3, False))
    print(neue_kombi.get_result()[1] + "=" + str(neue_kombi.get_result()[0]))

main()
