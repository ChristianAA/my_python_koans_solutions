#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas',
            'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(set(['MacLeod', 'Ramirez', 'Malcolm', 'Matunas']), there_can_only_be_only_one)

    def test_sets_are_unordered(self):
        self.assertEqual(set(['2', '3', '4', '1', '5']), set('12345'))

    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(['1', '2', '3', '4', '5'], sorted(set('13245')))

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = set(['MacLeod', 'Wallace', 'Willie'])
        warriors = set(['MacLeod', 'Wallace', 'Leonidas'])

        self.assertEqual(set(['Willie']), scotsmen - warriors) # (s - t) new set with elements in s but not in t
        self.assertEqual(set(['MacLeod', 'Wallace', 'Willie', 'Leonidas']), scotsmen | warriors)  # (s | t) new set with elements from both s and t
        self.assertEqual(set(['MacLeod', 'Wallace']), scotsmen & warriors) # (s & t) new set with elements common to s and t
        self.assertEqual(set(['Willie', 'Leonidas']), scotsmen ^ warriors) # (s ^ t) 	new set with elements in either s or t but not both

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in set([127, 0, 0, 1]))
        self.assertEqual(True, 'cow' not in set('apocalypse now'))

    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake')) # (s <= t ) test whether every element in s is in t
        self.assertEqual(True, set('cake').issubset(set('cherry cake'))) # (s <= t ) test whether every element in s is in t

        self.assertEqual(False, set('cake') > set('pie'))
