"""
This is a module used to illustrate working with custom modules.
This module is imported in 21-modules.py file as part of lesson demonstration.
"""

brand_colors = ('#e63946', '#41faee', '#a8dadc', '#1d3557')


def mean(nums):
    """function that takes a list of numbers and returns the average"""
    return sum(nums) / len(nums)
