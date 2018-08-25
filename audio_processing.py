import librosa
import numpy as np
from pathlib import Path

### AudioProcessor ###

class AudioProcessor:
    def __init__(self, sr, winsize_t):
        # define basic characteristics of audio and data
        self.defaultsr = sr # sampling rate
        self.winsize_t = winsize_t # size of window (in seconds)
        self.winsize_f = int(self.defaultsr*self.winsize_t) # size of window (in samples)

        # load all song files
        files_like = librosa.util.find_files('tastic_data/like/', ext=['mp3'])
        files_dislike = librosa.util.find_files('tastic_data/dislike/', ext=['mp3'])
        
        self.liked_songs_audio = []
        self.disliked_songs_audio = []

        # load and save all the audio in 2 arrays (liked, disliked)
        print("Loading audio files...")
        for y in files_like: 
            self.current_audio, current_sr = librosa.load(y)
            self.liked_songs_audio.extend(self.current_audio)
        self.liked_songs_audio = np.asarray(self.liked_songs_audio)
        print("Liked songs loaded.")
        
        for y in files_dislike: 
            current_audio, current_sr = librosa.load(y)   
            self.disliked_songs_audio.extend(current_audio)
        self.disliked_songs_audio = np.asarray(self.disliked_songs_audio)
        print("Disliked songs loaded.")

        # store the sizes (in samples) of the audio arrays
        self.n_samples_liked = len(self.liked_songs_audio)
        self.n_samples_disliked = len(self.disliked_songs_audio)

    def extractAllFeatures(self):
        features_liked = extractSongFeatures(self.liked_songs_audio, self.winsize_f, self.defaultsr)
        features_disliked = extractSongFeatures(self.disliked_songs_audio, self.winsize_f, self.defaultsr)
        return features_liked, features_disliked

class AudioTester:
    def __init__(self, sr, winsize_t):
        self.defaultsr = sr # sampling rate
        self.winsize_t = winsize_t # size of window (in seconds)
        self.winsize_f = int(self.defaultsr*self.winsize_t) # size of window (in samples)

        # load the file name of the song to test
        test_file = librosa.util.find_files('tastic_data/test/', ext=['mp3'])
        # load and save the audio
        self.title = Path(test_file[0]).name
        self.test_audio, current_sr = librosa.load(test_file[0])
        # store the size (in samples) of the audio file
        self.n_samples = len(self.test_audio)

    def extractAllFeatures(self):
        return extractSongFeatures(self.test_audio, self.winsize_f, self.defaultsr)


def extractSongFeatures(y, winsize, sr):
    ## Spectral features
    #Root-mean-square energy
    rms_energy = librosa.feature.rmse(y=y,frame_length=winsize,hop_length=winsize)
    # Mel-spectrogram
    mel_spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=winsize, hop_length=winsize)
    # Chromagram
    chromagr = librosa.feature.chroma_stft(y=y,sr=sr,n_fft=winsize,hop_length=winsize)
    # Cepstral coefficients
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_fft=winsize,hop_length=winsize)
    # Spectral centroid
    spectr_centroid = librosa.feature.spectral_centroid(y=y, sr=sr, n_fft=winsize, hop_length=winsize)
    # Spectral roll-off
    roll_off = librosa.feature.spectral_rolloff(y=y, sr=sr, n_fft=winsize, hop_length=winsize)
    # Bandwidth
    bw = librosa.feature.spectral_bandwidth(y=y, sr=sr, n_fft=winsize, hop_length=winsize)

    # return all features piled per window
    return np.vstack((rms_energy,mel_spect,chromagr,mfcc,spectr_centroid,roll_off,bw)).transpose()

