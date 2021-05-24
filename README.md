# PyPassGen - simple script to generate passwords

## Usage 
```delphi
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
```
