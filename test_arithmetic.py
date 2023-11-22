from arithmetic import pgcd
import unittest

def test_pgcd():
    assert pgcd(48, 18) == 6
    assert pgcd(1071, 462) == 21

if __name__ == "__main__":
    unittest.main()
