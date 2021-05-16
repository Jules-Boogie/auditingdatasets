"""
A simple function computing time elapsed

Author: Juliet George
Date:   9/7/2020
"""
import datetime


def past_a_week(d1,d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.

    If d1 is after d2, or less than a week has passed, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day.

    Parameter d1: The first event
    Precondition: d1 is EITHER a date objects or a datetime object

    Parameter d2: The first event
    Precondition: d2 is EITHER a date objects or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
    if type(d1) == type(d2):
        return (d2-d1) >= datetime.timedelta(days=7)
    else:
        if ((str(type(d1)).split("'"))[1]) == 'datetime.datetime':
            return (d2 - d1.date()) >= datetime.timedelta(days=7)
        elif ((str(type(d2)).split("'"))[1]) == 'datetime.datetime':
            return (d2.date() - d1) >= datetime.timedelta(days=7)
