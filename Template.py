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
    except:
        print("\nThere was a divide by zero error. Exiting\n")
        return
    

main()    