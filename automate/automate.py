#!/usr/bin/env python2
# @author = 01010011 01101000 01111001 01100001 01101101 01100001 01101100 
# date	  = 16/08/2016

"""
This script fills random names in the form of given website using mechanize library for 100 times.
To get details as form name and name of different fields of the form you can press Cltr+Shift+I on webpage
"""

from mechanize import Browser
import random

def main():

	br = Browser()

	names = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

	for i in range(100):
		br.set_handle_robots(False)
		br.open("http://www.ultimatelovecalc.com/love/1352035")
		br.select_form(name = "formMain")
		a1 = random.sample(names,5)
		a2 = random.sample(names,5)
		a3 = random.sample(names,5)
		br["fname"] = "".join(a1)
		br["cname1"] = "".join(a2)
		br["cname2"] = "".join(a3)
		br["cname3"] = "".join(a1)
		sub = br.submit()
		donech = sub.read()
		print i

if __name__ == "__main__":
	main()