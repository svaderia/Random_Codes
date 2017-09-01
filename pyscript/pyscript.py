#!/usr/bin/env python
# @author = 01010011 01101000 01111001 01100001 01101101 01100001 01101100 
# date	  = 08/06/2017

"""This script generates new python files with all the metadata getting filled automatically."""

# Import the modules needed to run the script.
from os.path import exists
from time import strftime
import sys

def main():
    # Checks if version is specified seprately or not
    version = -1    
    if len(sys.argv) > 1:
        if sys.argv[1] in ['2','3']:
            version = int(sys.argv[1])
        else:
            print('Version is not valid, so creating file with deafult version')
    
    title = input("Enter a title for your script: ")

    # Add .py to the end of the script.
    title = title + '.py'

    # Convert all letters to lower case.
    title = title.lower()

    # Remove spaces from the title.
    title = title.replace(' ', '_')

    # Check to see if the file exists to not overwrite it.
    if exists(title):
        print("\nA script with this name already exists.")
        exit(1)


    name = "53 68 79 61 6D 61 6C "

    # Create a file that can be written to.
    filename = open(title, 'w')

    # Set the date automatically.
    date = strftime("%d/%m/%Y")

    # Write the data to the file.
    if version > 0:
        filename.write('#!/usr/bin/env python{}'.format(str(version)))
    else:
        filename.write('#!/usr/bin/env python')
    string6 = \
"""

from __future__ import print_function
import sys

def input():
    # redefine input so that it works with both python2 and python3
    return sys.stdin.readline().rstrip()





def main():
    pass

if __name__ == "__main__":
    main()
"""
    string =\
"""


def main():
    pass

if __name__ == "__main__":
    main()
"""
    filename.write('\n# @author = ' + name)
    filename.write('\n# date\t  = ' + date)
    if version < 0:
        filename.write(string6)
    else:
        filename.write(string)
    # Close the file after writing to it.
    filename.close()

if __name__ == "__main__":
	main()