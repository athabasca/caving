#! usr/bin/python

import unittest
import lost_caver
from string import whitespace

class TestLostCaver(unittest.TestCase):

    def test_initial_position_regex(self):
        # Should handle different whitespace, all headings.
        pass_cases = [
            "(1,2) N", "(1, 2) N", "(1,2)N", "(7, 12)W",
            "(12, 12) E", "(2,2) S", "(9, 11)  W"
            ]
        for case in pass_cases:
            lost_caver.get_initial_position(case)
            
        # Should fail if malformed, negative ints, floats, bad headings.
        fail_cases = [
            "(1,2 N", "1, 2)E", "1,2 S", "1 2 E", "(-5, 7) S",
            "(-5, -5) W", "(12, -6) E", "(2.3, 3) E",
            "dgfgfd", "(a, b) N", "(2, 6) Q"
            ]
        for case in fail_cases:
            self.assertRaises(ValueError, lost_caver.get_initial_position, case)
            
    def test_coordinate_bounds(self):
        # 0<=x<20, 0<=y<16. Test internal and boundary values.
        pass_cases = [
            "(0, 0) N", "(0, 7) N", "(8, 0) N", "(5, 9) N",
            "(5, 15) N", "(19, 8) N", "(19, 15) N"
            ]
        for case in pass_cases:
            lost_caver.get_initial_position(case)
            
        fail_cases = [
            "(20, 0) N", "(0, 16) N", "(20, 16) N", "(233, 43) N",
            "(-5, 0) N", "(0, -7) N", "(-5, -9) N"
            ]
        for case in fail_cases:
            self.assertRaises(ValueError, lost_caver.get_initial_position, case)
            
    def test_move_caver(self):
        # move_caver(instruction, x, y, heading), heading as int 0-3
        # 0 - N, 1 - E, 2 - S, 3 - W
        exit_cases = [
            ('M', 5, 15, 0), ('M', 5, 0, 2),
            ('M', 19, 15, 1), ('M', 0, 15, 3)
            ]
        for case in exit_cases:
            self.assertRaises(SystemExit, lost_caver.move_caver, *case)
            
        turn_cases = [ # lists of parameter- and return-value-tuples
            [('L', 5, 15, 0), (5, 15, 3)], [('L', 5, 15, 3), (5, 15, 2)],
            [('L', 5, 15, 2), (5, 15, 1)], [('L', 5, 15, 1), (5, 15, 0)],
            [('R', 5, 15, 3), (5, 15, 0)], [('R', 5, 15, 2), (5, 15, 3)]
            ]
        for case in turn_cases:
            self.assertEqual(lost_caver.move_caver(*case[0]), case[1])
            
        for char in whitespace: # test that whitespace is ignored
            self.assertEqual(lost_caver.move_caver(char, 5, 5, 0), (5, 5, 0))
            
        bad_instructions = ['Q', ":", "RUN"]
        for inst in bad_instructions:
            self.assertRaises(ValueError, lost_caver.move_caver, *(inst, 5, 5, 0))
            
        type_error_instructions = [7, 2.5, -30]
        for inst in type_error_instructions:
            self.assertRaises(TypeError, lost_caver.move_caver, *(inst, 5, 5, 0))
            
if __name__ == '__main__':
    unittest.main()
