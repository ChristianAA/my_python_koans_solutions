#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice):

    # Variable for the total score
    score = 0;

    # Create a dict: Received set of rolls will be keys and we will assign'0' value to each key:

    # Example:
    # rolls = {}.fromkeys(set([1,2,3,4,5]), 0);  --> {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    # rolls = {}.fromkeys(set([1,2,2,1,4]), 0); --> {1: 0, 2: 0, 4: 0}
    rolls = {}.fromkeys(set(dice),0);

    # Count how many times appears a value in "dice" and increase the value in the dict for all the existing keys

    # Example:
    # set([1,2,2,1,4]) --> {1: 2, 2: 2, 4: 1}
    for number in dice:
        rolls[number] += 1

    # First scoring condition: A set of three ones is 1000 points.
    # If the "1" key exists and there are 3 or more "ones" in our rolls, add 1000 to the total score.
    # Then subtract 3 from key "1" (we need to add 100 for all the "ones" that are not part of a set of three)

    # Example
    # If there are 5 ones ([1,1,1,1,1]) --> {1: 5}
    # before: value = 5 score = 0,
    # after: value = 2 score = 1000. Then we will add (2 * 100 + 1000) to the total score (see 3º condition)
    if 1 in rolls and rolls[1] >= 3:
       score += 1000
       rolls[1] -= 3

    # Second scoring condition: A set of three numbers (other than ones) is worth 100 times the number.
    # If there are 3 or more "x" values in our rolls, add 100*x to the total score.
    # Then subtract 3 from key "x" (we need to add 50 for all the "fives" that are not part of a set of three,
    # as we did with "ones")
    for number in rolls:
        if rolls[number] >= 3:
            score += number * 100
            rolls[number] -= 3

    # Finally, third and fourth scoring conditions:
    for number in rolls:
        # Third scoring condition: A one (that is not part of a set of three) is worth 100 points.
        if number == 1:
            score += 100 * rolls[number]
        # Fourth scoring condition: A five (that is not part of a set of three) is worth 50 points.
        elif number == 5:
            score += 50 * rolls[number]

    return score


class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1,5,5,1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2,3,4,6]))

    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1,1,1]))

    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2,2,2]))
        self.assertEqual(300, score([3,3,3]))
        self.assertEqual(400, score([4,4,4]))
        self.assertEqual(500, score([5,5,5]))
        self.assertEqual(600, score([6,6,6]))

    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2,5,2,2,3]))
        self.assertEqual(550, score([5,5,5,5]))
        self.assertEqual(1150, score([1,1,1,5,1]))

    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1,2,2,2]))
        self.assertEqual(350, score([1,5,2,2,2]))