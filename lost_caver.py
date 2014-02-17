# 20 wide x 16 high cave, bottom left 0,0
# input: (x, y) <heading> <string of instructions>
# x, y integers, heading one of {N, E, S, W},
# each char of instructions one of {M, L, R}
# Denotes initial position/heading followed by directions.
# output: after each instruction is processed, print coordinates and heading.
#
# Things to note: falling off = death. i.e. 0 <= x <= 20, 0 <= y <= 16
# Can assume instructions will lead to exit of cave.

def main():
	""" docstring """
	
	get_inital_pos()
	
	get_dir()
	
	move()
	
	report_back()
	
if __name__ == '__main__':
	main()