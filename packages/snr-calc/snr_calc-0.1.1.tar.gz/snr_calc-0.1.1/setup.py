from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="snr_calc",
    version="0.1.1",
    description="A package to calculate SNR from audio files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anthony Soronnadi",
    author_email="anthony12soronnadi@gmail.com",
    packages=find_packages(),
    install_requires=[
        "librosa",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    test_suite='tests',
)
