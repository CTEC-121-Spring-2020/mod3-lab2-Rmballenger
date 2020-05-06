"""
CTEC 121
Robert Ballenger
Module 3 Lab 2
In Class Lab
"""

""" 
IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("There was a divide by zero error. Exiting.")
        exit
    except TypeError:
        print("type error")
        exit
    except:
        print("unknown exception")
        exit

main()