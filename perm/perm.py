#!/usr/bin/env python
# @author = 53 68 79 61 6D 61 6C 
# date	  = 09/08/2017

"""
This function prints all the permutation of the given list.
word: list of elements to permute
l: length of the list.
"""

from __future__ import print_function, division
import sys

def input():
    # redefine input so that it works with both python2 and python3
    return sys.stdin.readline().rstrip()

def perm(word, l = None):
    word = list(word)
    if l == None:
        l = len(word)
    if l == 0:
        print("".join(word))
        return
    for x in range(len(word) - l, len(word)):
        word[len(word) - l],word[x] = word[x], word[len(word) - l]
        perm(word, l-1)
        word[len(word) - l],word[x] = word[x], word[len(word) - l]

def main():
    word = input()
    perm(word)

if __name__ == "__main__":
    main()