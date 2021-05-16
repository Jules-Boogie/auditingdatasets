"""
A simple function comparing datetime objects.

Author: Juliet George
Date:   9/7/2020
"""
import datetime


def is_before(d1,d2):
    """
    Returns True if event d1 happens before d2.

    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day.

    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object

    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
    if type(d1) == type(d2):
        return d1 < d2
    else:
        if ((str(type(d1)).split("'"))[1]) == 'datetime.datetime':
            return d1.date() < d2
        elif ((str(type(d2)).split("'"))[1]) == 'datetime.datetime':
            return d1 <= d2.date()
