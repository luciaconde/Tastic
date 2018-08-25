import audio_processing
import song_download
import model_training
import model_testing

import librosa
import os

class options():
    def __init__(self, sr_train, sr_test, winsize_train, winsize_test):
        self.currentModel = None
        # parameters for training data
        # sr = sampling rate
        # winsize = size of window (in seconds) for the division in frames of the audio signal
        self.sr_train = sr_train
        # parameters for testing data
        self.winsize_train = winsize_train
        self.sr_test = sr_test
        self.winsize_test = winsize_test
        
        # predictions are run on each frame
        # the class that was predicted the most is chosen as the overall prediction for the whole song


    def downloadSongs(self):
        song_liked1 = input("Enter a YouTube link to a song you like: ")
        song_liked2 = input("Great! Enter a YouTube link to a second song you like: ")
        song_disliked1 = input("Almost there! Enter a YouTube link to a song you dislike: ")
        song_disliked2 = input("And finally, enter a YouTube link to a second song you dislike: ")

        # download all songs
        print("Downloading songs...")
        song_download.downloadSong(song_liked1, True)
        song_download.downloadSong(song_liked2, True)
        song_download.downloadSong(song_disliked1, False)
        song_download.downloadSong(song_disliked2, False)

    def testModel(self):
        song_test = input("Now, enter a YouTube link to any song you want me to predict your taste on: ")

        # load the test song and extract its features
        song_download.downloadTestSong(song_test)
        print("Processing test song audio...")
        at = audio_processing.AudioTester(self.sr_test, self.winsize_test)
        features_test = at.extractAllFeatures()
        print("Test song processed.")

        # run the model for the test song
        mtest = model_testing.ModelTester(features_test, self.currentModel, at.title)
        print("DONE! The overall prediction is: ",mtest.predictTaste())

        # verify prediction and move test song to training data
        true_taste = input("Was that right? Can you tell me if you actually liked or disliked that song? [write like or dislike]: ")
        mtest.verifyPrediction(true_taste)

    def createModel(self):
        # load all the audio (liked, disliked) and perform feature extraction
        ap = audio_processing.AudioProcessor(self.sr_train, self.winsize_train)
        features_liked, features_disliked = ap.extractAllFeatures()

        # train the random regression forest
        print("Creating the predictive model...")
        mt = model_training.ModelTrainer(features_liked, features_disliked, ap.n_samples_liked, ap.n_samples_disliked, ap.winsize_f)
        self.currentModel = mt.fitRRForest()
        print("The predictive model is ready!")

    def createNewModel(self):
        print("Hi there! Let's get to know your music taste...")
        self.downloadSongs()
        self.createModel()
        self.testModel()

    def continueModel(self):
        if self.verifyExistingData():
            self.createModel()
            self.testModel()

    def testCurrentModel(self):
        if self.verifyExistingData():
            self.testModel()

    def verifyExistingData(self):
        files_like = librosa.util.find_files('tastic_data/like/', ext=['mp3'])
        files_dislike = librosa.util.find_files('tastic_data/dislike/', ext=['mp3'])

        if not files_like or not files_dislike:
            print("There are not enough stored songs to continue building a model!")
            return False
        elif self.currentModel == None:
            print("No model has been built yet!")
            return False
        else:
            return True

    def deleteAllData(self):
        files_like = librosa.util.find_files('tastic_data/like/', ext=['mp3'])
        files_dislike = librosa.util.find_files('tastic_data/dislike/', ext=['mp3'])
        files_test = librosa.util.find_files('tastic_data/test/', ext=['mp3'])

        files_all = files_like + files_dislike + files_test
    
        for y in files_all:
            try:
                os.remove(y)
            except FileNotFoundError:
                pass
        print("Data deleted.")
  
