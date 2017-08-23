#!/usr/bin/env python
# @author = 53 68 79 61 6D 61 6C 
# date	  = 09/08/2017

"""This script checks the validity of Birthday paradox."""

from __future__ import print_function, division
import sys

def input():
    # redefine input so that it works with both python2 and python3
    return sys.stdin.readline().rstrip()

def genBday(n):
    from datetime import date, timedelta
    import random
    # Assuming you want a random day of the current year
    firstJan = date.today().replace(day=1, month=1) 
    bdaylist = [firstJan + timedelta(days = random.randint(0, 365)) for i in range(n)]
    return [(x.day, x.month) for x in bdaylist]

def getProbability(n, T):
    match = 0
    for i in range(T):
        lst = genBday(n)
        if len(lst) != len(set(lst)):
            match +=1
    return match/T

def main():
    n,T = [int(x) for x in input().split()]
    print(getProbability(n, T))    

if __name__ == "__main__":
    main()