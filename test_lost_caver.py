#! usr/bin/python

import unittest
import lost_caver

class TestLostCaver(unittest.TestCase):

    def test_no_input(self):
        # Should raise an exception if no input given.
        self.assertRaises(EOFError, lost_caver.main, "")
    
    def test_initial_position_regex(self):
        # Should handle different whitespace, all headings.
        pass_cases = ["(1,2) N", "(1, 2) N", "(1,2)N", "(7, 12)W",
                        "(12, 12) E", "(2,2) S", "(9, 11)  W"]
        for case in pass_cases:
            lost_caver.main(case)
            
        # Should fail if malformed, negative ints, floats, bad headings.
        fail_cases = ["(1,2 N", "1, 2)E", "1,2 S", "1 2 E", "(-5, 7) S",
                        "(-5, -5) W", "(12, -6) E", "(2.3, 3) E",
                        "dgfgfd", "(a, b) N", "(2, 6) Q"]
        for case in fail_cases:
            self.assertRaises(ValueError, lost_caver.main, case)
            
    def test_coordinate_bounds(self):
        # 0<=x<20, 0<=y<16. Test internal and boundary values.
        pass_cases = ["(0, 0) N", "(0, 7) N", "(8, 0) N", "(5, 9) N",
                        "(5, 15) N", "(19, 8) N", "(19, 15) N"]
        for case in pass_cases:
            lost_caver.main(case)
            
        fail_cases = ["(20, 0) N", "(0, 16) N", "(20, 16) N", "(233, 43) N",
                        "(-5, 0) N", "(0, -7) N", "(-5, -9) N"]
        for case in fail_cases:
            self.assertRaises(ValueError, lost_caver.main, case)
            
if __name__ == '__main__':
    unittest.main()
