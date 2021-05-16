"""
Functions for working with datetime objects.

Author: Juliet George
Date:   9/7/2020
"""
import datetime


def christmas_day(year):
    """
    Returns ISO day of the week for Christmas in the given year.

    The ISO day is an integer between 1 and 7.  It is 1 for Monday, 7 for Sunday
    and the appropriate number for any day in-between.

    Parameter year: The year to check for Christmas
    Precondition: years is an int > 0 (and a year using the Gregorian calendar)
    """
    # HINT: Make a date object and use the isoweekday method
    test = datetime.date(year,12,25)
    return test.weekday() + 1


def iso_str(d,t):
    """
    Returns the ISO formatted string of data and time together.

    When combining, the time must be accurate to the microsecond.

    Parameter d: The month-day-year
    Precondition: d is a date object

    Parameter t: The time of day
    Precondition: t is a time object
    """
    # HINT: Combine date and time into a datetime and use isoformat
    my_date = datetime.datetime(d.year,d.month,d.day,t.hour,t.minute,t.second,t.microsecond)
    my_date_iso = my_date.isoformat()
    return my_date_iso
