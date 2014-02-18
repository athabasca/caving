#! usr/bin/python

# 20 wide x 16 high cave, bottom left 0,0
# input: (x, y) <heading> <string of instructions>
# x, y integers, heading one of {N, E, S, W},
# each char of instructions one of {M, L, R}
# Denotes initial position/heading followed by directions.
# output: after each instruction is processed, print coordinates and heading.
#
# Things to note: falling off = death. i.e. 0 <= x < 20, 0 <= y < 16
# Can assume instructions will lead to exit of cave.

from sys import stdin # Assuming input is text stream from stdin.
import re

debug = True

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
        msg = "Need initial position and heading: (x, y) <h>\nLine: {0}\n"\
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
    """ Get caver's new location given an instruction. """
    
    if instruction == 'M': # Move 1 in faced direction.
        if heading == 0:
            y += 1
        elif heading == 1:
            x += 1
        elif heading == 2:
            y -= 1
        elif heading == 3:
            x -= 1
        # Check if caver fell off the edge.
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
    else:
        print "Invalid instruction: {0}".format(instruction)
    
    print "({0}, {1}) {2}".format(x, y, headings[heading])    
    return (x, y, heading)

    
def main():
    """ docstring """
    
    # Assuming initial coordinates and heading are on one line.
            
    line = stdin.readline()
    
    if line == "": # no input given
        raise EOFError("No input.")

    line = "".join(line.strip().split()) # Strip all whitespace.
    
    x, y, heading = get_initial_position(line)
            
    start = line.index(heading) + 1 # index of first instruction
    instructions = line[start:]

    # Encode heading as int. N = 0, E = 1, S = 2, W = 3
    heading = headings.index(heading)    
    
    for instruction in instructions:
        x, y, heading = move_caver(instruction, x, y, heading)
        
	
if __name__ == '__main__':
    main()
