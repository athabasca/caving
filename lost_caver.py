#! usr/bin/python

# lost_caver.py
# Author: Athabasca Witschi
# Date: February, 2014
# 
# About: The goal is to guide a caver to safety by sending him
# his position and heading and then directions to the exit of the cave.
#
# 20 wide x 16 high cave, bottom left is at (0,0)
# Input: (x, y) <heading> <string of instructions>
# x, y are integers, heading is one of {N, E, S, W},
# each character of instructions  is one of {M, L, R}.
# Note: (x, y) <heading> must be on one line.
#
# Output: after each instruction is processed, coordinates
# and heading are printed. If you go off the edge, a death
# message is printed. Otherwise, once there is no more input,
# you will get a success message.

from sys import stdin, exc_info
import re

debug = False

# List that maps headings to ints (the indices)
headings = ['N', 'E', 'S', 'W']

def get_initial_position(line):
    """ Get initial position and heading from input line. """
    
    matchobj = re.match(r"\((\d+),\s*(\d+)\)\s*([NESW])", line)
    if matchobj:
        x, y, heading = matchobj.groups()
        x, y = int(x), int(y) # safe since regex only matches digits for x, y
        
        if debug:
            print "x: {0}, y: {1}, heading: {2}".format(x, y, heading)
    else:
        msg = "Need initial position and heading: (x, y) <h>\nInput line: {0}\n"\
                .format(line)
        raise ValueError(msg)
    
    # Check bounds of initial coordinates.
    if x < 0 or x >= 20:
        msg = "x out of bounds (0 <= x < 20). x: {0}".format(x)
        raise ValueError(msg)
    if y < 0 or y >= 16:
        msg = "y out of bounds (0 <= y < 16). y: {0}".format(y)
        raise ValueError(msg)
        
    return (x, y, heading)

    
def move_caver(instruction, x, y, heading):
    """ Get caver's new location given an instruction, print position. """
    
    if type(instruction) is not str:
        raise TypeError("Invalid instruction: {0}\n".format(instruction))
        
    if instruction == 'M': # Move 1 in faced direction.
        if heading == 0:
            y += 1
        elif heading == 1:
            x += 1
        elif heading == 2:
            y -= 1
        elif heading == 3:
            x -= 1
        # Check if caver fell off the edge. Fatal error. Ahaha.
        if x < 0 or x >= 20 or y < 0 or y >= 16:
            print "AAAAAaaa...."
            print "This is the sound the caver makes",
            print "as he falls to his death."
            exit(0)
            
    elif instruction == 'L': # Turn left.
        heading -= 1
        if heading == -1:
            heading = 3
    elif instruction == 'R': # Turn right.
        heading += 1
        if heading == 4:
            heading = 0
    elif instruction.isspace():
        return (x, y, heading)
    else:
        raise ValueError("Invalid instruction: {0}\n".format(instruction))
    
    print "({0}, {1}) {2}".format(x, y, headings[heading])    
    return (x, y, heading)

    
def main():
    """ Guide a caver through a cave to the exit (or his death). """
    
    # Assuming initial coordinates and heading are on one line.
            
    line = stdin.readline()
    
    if line == "": # no input given
        print "Usage: (x, y) <heading> <instructions>"
        exit(0)

    line = "".join(line.strip().split()) # Strip all whitespace.
    
    try:
        x, y, heading = get_initial_position(line)
    except ValueError:
        print "Error: ",
        print exc_info()[1]
        exit(1)
            
    start = line.index(heading) + 1 # index of first instruction
    instructions = line[start:]

    # Encode heading as int. N = 0, E = 1, S = 2, W = 3
    heading = headings.index(heading)    
    
    for instruction in instructions:
        try:
            x, y, heading = move_caver(instruction, x, y, heading)
        except (TypeError, ValueError):
            print "Error: ",
            print exc_info()[1]
            exit(1)
        
    # Any subsequent lines from stdin should just be instructions.
    instruction = stdin.read(1)
    while (instruction != ""): # while not EOF
        try:
            x, y, heading = move_caver(instruction, x, y, heading)
        except (TypeError, ValueError):
            print "Error: ",
            print exc_info()[1]
            exit(1)
            
        instruction = stdin.read(1)
        
    print "The caver made it to the exit at ({0}, {1})!".format(x, y)
    exit(0)
        
        	
if __name__ == '__main__':
    main()
