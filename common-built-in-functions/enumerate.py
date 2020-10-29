# ------------------------------------------------------------------------------------
# Tutorial: brief description of tutorial content
# ------------------------------------------------------------------------------------

# Enums are set of symbolic names bound to unique constant values.
# Example, we can have Month enumeration with 12 months

from enum import Enum

class Month(Enum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12

# Access via Name

feb_elem = Month.FEB

print("Number for Month {name} is {value}".format(name=feb_elem.name,
                                                  value=feb_elem.value))

# Access via Value

feb_elem = Month(2)

print("Number for Month {name} is {value}".format(name=feb_elem.name,
                                                  value=feb_elem.value))


# ------------------------------------------------------------------------------------
# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# ------------------------------------------------------------------------------------

# # Challenge 1: Create Enum which store Day of week and Color as value for each day
# # Replace the question(?) with logic

# class ColorWeek(?):
#     MONDAY = 'RED'
#     TUESDAY = 'GREEN'
#     WEDNESDAY = 'BLUE'
#     THURSDAY = 'CYAN'
#     FRIDAY = 'YELLOW'
#     SATURDAY = 'WHITE'
#     SUNDAY = 'BLUE'

# if ColorWeek.MONDAY.value == ?:
#     print("Color for Monday is RED")

# # Print the day when color is GREEN
# print("Day with color GREEN is: ")
# print(?)
