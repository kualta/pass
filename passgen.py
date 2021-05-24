#! /usr/bin/python

import sys
import getopt
import string
import random

usage = """
PyPassGen - simple script to generate passwords

usage: passgen.py <operation>

operations:
  -e, --easy        Generate easy password (6 char.)
  -m, --medium      Generate medium password (10 char.)
  -h, --hard        Generate hard password (16 char.)
  --custom=X        Generate password with X characters
  --letters-only=X  Generate password using only letters
  --pin=X           Generate PIN-code
  --help            Show this message

note:
  X - amount of characters (int), default=4  
"""

items = string.ascii_letters + string.digits


def getPass(mode = "password", complexity = 4):
    out = ""
    
    if (mode == "password"):
        for x in range(complexity):
            out += random.choice(items)
    if (mode == "lo"):
        for x in range(complexity):
            out += random.choice(string.ascii_letters)
    if (mode == "pin"):
        for x in range(complexity):
                out += random.choice(string.digits)
    print(out)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "emh", ["easy", "medium", "hard", "custom=", "letters-only=", "pin=", "help"])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--help':
            print(usage)
            sys.exit()
        elif opt in ("-e", "--easy"):
            getPass(complexity=6)
        elif opt in ("-m", "--medium"):
            getPass(complexity=10)
        elif opt in ("-h", "--hard"):
            getPass(complexity=16)
        elif opt == "--custom":
            getPass(complexity=int(arg))
        elif opt == '--letters-only':
            getPass(mode="lo", complexity=int(arg))
        elif opt == '--pin':
            getPass(mode="pin", complexity=int(arg))

if __name__ == "__main__":
    main(sys.argv[1:])
