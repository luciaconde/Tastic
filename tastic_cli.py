import audio_processing
import song_download
import model_training
import model_testing

import librosa
import os

def menu():       ## Your menu design here
    print(10 * "-", "TASTIC: a machine learning-based music taste predictor", 10 * "-")
    print("1. New model")
    print("2. Continue model")
    print("3. Delete all data")
    print("4. Exit")
    print(76 * "-")

def downloadSongs():
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

def createModel():
    # parameters for training data
    sr_train = 22050
    winsize_train = 1
    # parameters for testing data
    sr_test = 22050 # sampling rate of the song audio file to be tested
    winsize_test = 2 # size of window (in seconds) for the division in frames of the audio signal
    # predictions are run on each frame
    # the class that was predicted the most is chosen as the overall prediction for the whole song

    # load all the audio (liked, disliked) and perform feature extraction
    ap = audio_processing.AudioProcessor(sr_train, winsize_train)
    features_liked, features_disliked = ap.extractAllFeatures()

    # train the random regression forest
    print("Creating the predictive model...")
    mt = model_training.ModelTrainer(features_liked, features_disliked, ap.n_samples_liked, ap.n_samples_disliked, ap.winsize_f)
    model = mt.fitRRForest()
    print("Model created.")

    print("The predictive model is ready!")
    song_test = input("Now, enter a YouTube link to any song you want me to predict your taste on: ")

    # load the test song and extract its features
    song_download.downloadTestSong(song_test)
    print("Processing test song audio...")
    at = audio_processing.AudioTester(sr_test, winsize_test)
    features_test = at.extractAllFeatures()
    print("Test song processed.")

    # run the model for the test song
    mtest = model_testing.ModelTester(features_test, model, at.title)
    print("DONE! The overall prediction is: ",mtest.predictTaste())

    # verify prediction and move test song to training data
    true_taste = input("Was that right? Can you tell me if you actually liked or disliked that song? [write like or dislike]: ")
    mtest.verifyPrediction(true_taste)

def createNewModel():
    print("Hi there! Let's get to know your music taste...")
    downloadSongs()
    createModel()

def continueModel():
    if verifyExistingData():
        createModel()

def verifyExistingData():
    files_like = librosa.util.find_files('like/', ext=['mp3'])
    files_dislike = librosa.util.find_files('dislike/', ext=['mp3'])

    if not files_like or not files_dislike:
        print("There are not enough stored songs to continue building a model!")
        return False
    else:
        return True


def deleteAllData():
    files_like = librosa.util.find_files('like/', ext=['mp3'])
    files_dislike = librosa.util.find_files('dislike/', ext=['mp3'])
    files_test = librosa.util.find_files('test/', ext=['mp3'])

    files_all = files_like + files_dislike + files_test
    
    for y in files_all:
        try:
            os.remove(y)
        except FileNotFoundError:
            pass
    print("Data deleted.")
  
app_open = True      
  
while app_open:
    menu()    # display menu
    option = int(input("Enter your choice [1-4]: "))
     
    if option == 1:     
        print(5 * "-", "Creating new model...", 5 * "-")
        createNewModel()
    elif option == 2:
        print(5 * "-", "Continuing model...", 5 * "-")
        continueModel()
    elif option == 3:
        print(5 * "-", "Deleting all data...", 5 * "-")
        deleteAllData()
    elif option == 4:
        print(5 * "-", "Closing Tastic...", 5 * "-")
        app_open = False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong one, we don't have that many options! Please choose another one.")
