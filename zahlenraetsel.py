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
        self.calc_rule = 0
        self.dice = []

    def __str__(self):
        return self.calc_string

    def get_result(self):
        """ returns result and string """

        return self.result, self.calc_string

    def add_dice(self, dice):
        """ add a dice to the Combination """

        self.dice = dice
        if len(self.dices) < 4:
            self.dices.append(dice)
        else:
            print("max. 4 Würfel pro Kombination!")



       # if brackets have to be written,
       # we insert them here in the string according to math rules
       #if self.dice.calc > self.calc_rule:
            # logging.debug(position.calc)
            # logging.debug(self.calc_rule)
            #self.calc_string = "(" + self.calc_string + ")"
            # logging.debug(self.calc_string)

        if self.dice.calc == 0:
            self.result = self.result + self.dice.side
            if self.calc_string == "":
                self.calc_string = str(self.dice.side)
            else:
                self.calc_string = self.calc_string + "+" + str(self.dice.side)
                self.calc_rule = 1
        elif self.dice.calc == 1:
            self.result = self.result - self.dice.side
            self.calc_string = self.calc_string + "-" + str(self.dice.side)
            self.calc_rule = 1
        elif self.dice.calc == 2:
            self.result = self.result * self.dice.side
            self.calc_string = self.calc_string + "*" + str(self.dice.side)
            self.calc_rule = 3
        elif self.dice.calc == 3:
            self.result = self.result / self.dice.side
            self.calc_string = self.calc_string + "/" + str(self.dice.side)
            self.calc_rule = 3
        elif self.dice.calc == 4:
            self.result = self.result ** self.dice.side
            self.calc_string = self.calc_string + "**" + str(self.dice.side)
            self.calc_rule = 4
        else:
            print("Error")

        # logging.debug(self.result)




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
    logging.debug("%s, %s", number1, number2)

    # use itertools, to have less nested loops
    for positions in itertools.product(number_set, repeat=4):
        logging.debug("%s, %s, %s, %s", positions[0], positions[1], positions[2], positions[3])
        #only calculate, if number 1 and number 2 are used twice
        if (positions[0]+positions[1]+positions[2]+positions[3]) == (number1*2 + number2*2):
            if positions[0] is result:
                # Combinations with only one dice don't need a Combination class
                result_set.add(str(positions[0]))
                logging.debug("%s ergibt %s", positions[0], positions[0])

            for calc_type2 in range(0, 5):
                kombination = Combination()
                kombination.add_dice(Dice(positions[0], 0, False))
                kombination.add_dice(Dice(positions[1], calc_type2, False))
                kombination_erg = kombination.get_result()

                if kombination_erg[0] is result:
                    result_set.add(kombination_erg[1])
                    logging.debug("%s ergibt %s",
                                  kombination_erg[1], kombination_erg[0])

                logging.debug("%s, %s, %s", positions[0], positions[1], positions[2])

                for calc_type3 in range(0, 5):
                    kombination3 = Combination()
                    kombination3.add_dice(Dice(positions[0], 0, False))
                    kombination3.add_dice(Dice(positions[1], calc_type2, False))
                    kombination3.add_dice(Dice(positions[2], calc_type3, False))
                    kombination3_erg = kombination3.get_result()

                    if kombination3_erg[0] is result:
                        result_set.add(kombination3_erg[1])
                        logging.debug("%s ergibt %s",
                                      kombination3_erg[1], kombination3_erg[0])

                    logging.debug("%s, %s, %s, %s",
                                  positions[0], positions[1], positions[2], positions[3])
                    for calc_type4 in range(0, 5):
                        kombination4 = Combination()
                        kombination4.add_dice(Dice(positions[0], 0, False))
                        kombination4.add_dice(Dice(positions[1], calc_type2, False))
                        kombination4.add_dice(Dice(positions[2], calc_type3, False))
                        kombination4.add_dice(Dice(positions[3], calc_type4, False))
                        kombination4_erg = kombination4.get_result()

                        if kombination4_erg[0] is result:
                            result_set.add(kombination4_erg[1])
                            logging.debug("%s ergibt %s", kombination4_erg[1], kombination4_erg[0])

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
