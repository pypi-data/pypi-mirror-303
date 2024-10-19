import unittest
from snr_package.snr_calc import process_audio_file, process_directory

class TestSNRCalculator(unittest.TestCase):
    
    def test_process_audio_file(self):
        snr = process_audio_file('tests/sample_directory/silent_audio.wav', signal_freq_range=(300, 3000), sample_rate=8000)
        self.assertIsNotNone(snr, "SNR should not be None")
        self.assertIsInstance(snr, (float, int), "SNR should be a numeric value")

    def test_process_directory(self):
        results = process_directory('tests/sample_directory', signal_freq_range=(300, 3000), sample_rate=8000)
        self.assertIsInstance(results, dict, "Results should be a dictionary")
        for file, snr in results.items():
            self.assertIsNotNone(snr, f"SNR for {file} should not be None")

if __name__ == '__main__':
    unittest.main()
