#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if a == b == c:
        return 'equilateral'
    elif a == b or a == c or b == c:
        return 'isosceles'
    return 'scalene'

# "Oficial solution" for about_triangle_project.py
#
#   sides = sorted([a, b, c])
#   unique_sides = sorted(set(sides))
#
#   if len(unique_sides) == 1:
#       return 'equilateral'
#   elif len(unique_sides) == 2:
#       return 'isosceles'
#   elif len(unique_sides) == 3:
#       return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
