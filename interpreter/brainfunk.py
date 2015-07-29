# Brainfunk 
#
# Original Brainfuck Interpreter
# Copyright 2011 Sebastian Kaspari
#
# Brainfunk Interpreter Edition and Brainfunk changes
# Copyright 2015 Jack Heikell
#
# Usage: ./brainfuck.py [FILE]

import sys
import getch

def execute(filename):
  f = open(filename, "r")
  evaluate(f.read())
  f.close()


def evaluate(code):
  code     = cleanup(list(code))
  bracemap = buildbracemap(code)

  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    command = code[codeptr]

    if command == "Toot":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "Doot":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "TootToot":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "TootTootToot":
      cells[cellptr] = cells[cellptr] + 10 if (cells[cellptr] + 10) < 255 else 0

    if command == "DootDoot":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "DootDootDoot":
      cells[cellptr] = cells[cellptr] - 1 if(cells[cellptr] - 10) > 0 else 255

    if command == "DootDootDo":
      cells[cellptr] = cells[cellptr] - 5 if(cells[cellptr] - 5) > 0 else 255

    if command == "TootTootTo":
      cells[cellptr] = cells[cellptr] + 5 if(cells[cellptr] + 5) > 0 else 255

    if command == "Brap":
      cells[cellptr] = 0

    if command == "Prap":
      cells[cellptr] = 255

    if command == "Plap" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "Blap" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == "Parp": sys.stdout.write(chr(cells[cellptr]))
    if command == "Honk": cells[cellptr] = ord(getch.getch())
      
    codeptr += 1


def cleanup(code):
  return filter(lambda x: x in ['Toot', 'Doot', 'TootToot', 'TootTootToot', 'DootDoot', 'DootDootDoot', 'Brap', 'Prap', 'Plap', 'Blap', 'Parp', 'Honk', 'DootDootDo', 'TootTootTo'], code)


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "Plap": temp_bracestack.append(position)
    if command == "Blap":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap


def main():
  if len(sys.argv) == 2: execute(sys.argv[1])
  else: print "Usage:", sys.argv[0], "filename"

if __name__ == "__main__": main()

