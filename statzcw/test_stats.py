import unittest
import stats
import statistics

class MyTestCase(unittest.TestCase):

    def test_zcount(self):
        list_input = [1, 8, 5, 3, 17, 53]
        expected = 6
        actual = stats.zcount(list_input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_zmean(self):
        list_input = [1, 8, 5, 3, 17, 53]
        expected = statistics.mean(list_input)
        actual = stats.zmean(list_input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_zmode(self):
        list_input = [1, 8, 5, 3, 17, 53]
        expected = statistics.mode(list_input)
        actual = stats.zmode(list_input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_zvariance(self):
        list_input = [1, 8, 5, 3, 17, 53]
        expected = statistics.variance(list_input)
        actual = stats.zvariance(list_input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_zstddev(self):
        list_input = [1, 8, 5, 3, 17, 53]
        expected = statistics.stdev(list_input)
        actual = stats.zstddev(list_input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_zcorr(self):
        x = [1,2,3]
        y = [3,2,1]
        expected = statistics.correlation(x, y)
        actual = stats.zcorr(x, y)
        self.assertEqual(expected, actual)  # add assertion here

if __name__ == '__main__':
    unittest.main()
