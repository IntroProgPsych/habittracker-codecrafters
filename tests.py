#import all needed modules here
import unittest
from app import interpret_score

#write all your tests below this line
from app import interpret_score

class TestInterpretScore(unittest.TestCase):
    def test_low(self):
        self.assertEqual(interpret_score(0), "Low")
        self.assertEqual(interpret_score(5), "Low")

    def test_moderate(self):
        self.assertEqual(interpret_score(6), "Moderate")
        self.assertEqual(interpret_score(11), "Moderate")

    def test_high(self):
        self.assertEqual(interpret_score(12), "High")
        self.assertEqual(interpret_score(20), "High")


#write your test suite here, in the main() function
def main():
    #call all your tets here, one on each line
    print("Starting tests suite...")
    suite = unittest.TestSuite()
    suite.addTest(TestInterpretScore("test_interpret_score_high"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
#please do not change the lines below
if __name__ == "__main__":
    main()
