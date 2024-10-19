# Signal to Noise Ratio Calculation -

A Python package for calculating the Signal-to-Noise Ratio (SNR) of audio files. It supports processing individual audio files or all audio files within a directory and allows users to specify the frequency range of the signal.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Calculating SNR for a Single File](#calculating-snr-for-a-single-file)
  - [Calculating SNR for All Files in a Directory](#calculating-snr-for-all-files-in-a-directory)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Features

- Calculate SNR for individual audio files or for all files in a directory.
- Supports custom signal frequency ranges and sample rates.
- Handles common audio formats like WAV, MP3, and FLAC.

## Installation

1. Clone the repository or download the package.
2. Navigate to the package directory and run:

    ```bash
    pip install .
    ```

Alternatively, if the package is available on PyPI, you can install it directly using:

```bash
pip install snr_calc
```
## Usage

### Calculating SNR for a Single File

```bash
from snr_calc import process_audio_file

# Specify the path to the audio file
audio_file_path = "path/to/your/audio_file.wav"

# Calculate SNR with a custom signal frequency range and sample rate
snr_value = process_audio_file(audio_file_path, signal_freq_range=(500, 4000), sample_rate=None)

# Display the SNR result
if snr_value is not None:
    print(f"SNR for {audio_file_path}: {snr_value} dB")
else:
    print("Failed to calculate SNR.")
```

### Calculating SNR for All Files in a Directory

```bash
from snr_calc import process_directory

# Specify the path to the directory
directory_path = "path/to/your/audio_directory"

# Calculate SNR for all audio files in the directory
snr_results = process_directory(directory_path, signal_freq_range=(500, 4000), sample_rate=None)

# Display the SNR results for each file
if snr_results:
    for file_name, snr_value in snr_results.items():
        print(f"File: {file_name}, SNR: {snr_value} dB")
else:
    print("No audio files found or failed to calculate SNR.")
```

## Requirements
- Python 3.10 or higher
- Required Python packages:
  - librosa
  - numpy
  - scipy

These dependencies are automatically installed when you install the package via pip.

## Contributing

Contributions are welcome! If you want to contribute to the development of this package:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Create a Pull Request.

Please ensure your code passes all existing tests and add new tests if necessary.

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.


### Explanation

- **Overview:** Gives a brief description of the package and its purpose.
- **Table of Contents:** Provides easy navigation within the README.
- **Features:** Highlights key features of the package.
- **Installation:** Details how to install the package.
- **Usage:** Includes code snippets to demonstrate how to use the package for single files and directories.
- **Requirements:** Lists package dependencies.
- **Contributing:** Offers guidelines for developers who want to contribute to the package.
- **License:** States the license under which the package is distributed. Adjust it as needed.