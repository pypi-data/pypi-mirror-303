import librosa
import numpy as np
import os

def calculate_snr(y, sr, signal_freq_range=(300, 3000)):
    """
    Calculates SNR from a loaded audio signal.
    
    Args:
        y: The audio signal.
        sr: Sample rate of the audio signal.
        signal_freq_range: Frequency range of the signal in Hz (default 300–3000 Hz).

    Returns:
        SNR in dB or None on error.
    """
    try:
        # Compute power spectrogram
        S = np.abs(librosa.stft(y))**2
        
        # Get frequency bins
        freqs = librosa.fft_frequencies(sr=sr)
        
        # Map frequency range to spectrogram indices
        signal_indices = np.where((freqs >= signal_freq_range[0]) & (freqs <= signal_freq_range[1]))[0]
        
        # Calculate signal power
        signal_power = np.sum(S[signal_indices, :])
        
        # Calculate total power and noise power
        total_power = np.sum(S)
        noise_power = total_power - signal_power
        
        # Handle edge case
        if noise_power <= 0:
            return float('inf')
        
        # Calculate SNR in dB
        snr = 10 * np.log10(signal_power / noise_power)
        return snr
    except Exception as e:
        print(f"Error calculating SNR: {e}")
        return None

def process_audio_file(file_path, signal_freq_range=(300, 3000), sample_rate=None):
    """
    Load an audio file and calculate the SNR.
    
    Args:
        file_path: Path to the audio file.
        signal_freq_range: Frequency range of the signal (in Hz).
        sample_rate: Sampling rate for loading the audio (default 8000).
    
    Returns:
        SNR in dB or None on error.
    """
    try:
        y, sr = librosa.load(file_path, sr=sample_rate)
        return calculate_snr(y, sr, signal_freq_range)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

def process_directory(directory_path, signal_freq_range=(300, 3000), sample_rate=None):
    """
    Process all audio files in a directory to calculate SNR.
    
    Args:
        directory_path: Path to the directory containing audio files.
        signal_freq_range: Frequency range of the signal (in Hz).
        sample_rate: Sampling rate for loading the audio (default 8000).

    Returns:
        A dictionary with filenames as keys and SNR values as values.
    """
    snr_results = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.wav', '.mp3', '.flac')):
                file_path = os.path.join(root, file)
                snr = process_audio_file(file_path, signal_freq_range, sample_rate)
                snr_results[file] = snr
    return snr_results
