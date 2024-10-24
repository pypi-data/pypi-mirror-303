import unittest
from itertools import permutations
from numpy import array
from src.nanotracking import DifferencePlotter

samples = ["1-1e5 150nm Nanosphere", "1-1e5 150nm Nanosphere 2", "1-1e5 150nm Nanosphere 32ms", "1-1e5 150nm Nanosphere diff detection setting"]  

class Test_Basics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        nta = DifferencePlotter.NTA(
            output_folder = "tests/Test output/Basics",
            truncation_size = 400 # nanometers
        )
        nta.load(
            datafolder = "tests/Test data",
            filenames = samples
        )
        cls.nta = nta
    def test_compute(self):
        self.nta.compute()
    def test_compare(self):
        self.nta.compute()
        self.nta.compare()
    def plot_samples(self, num_samples):
        sample_array = array(samples)
        for indices in permutations(range(len(samples)), num_samples):
            indices = array(indices)
            self.nta.plot(*sample_array[indices], name = f"Sample indices {indices}")
    def test_plot_1_sample(self):
        self.plot_samples(1)
    def test_plot_2_samples(self):
        self.plot_samples(2)
    def test_plot_3_samples(self):
        self.plot_samples(3)
    def test_plot_4_samples(self):
        self.plot_samples(4)

if __name__ == '__main__':
    unittest.main()
