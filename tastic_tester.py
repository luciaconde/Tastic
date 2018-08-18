import audio_processing
import model_training
import model_testing

### MAIN APPLICATION DRAFT ###
# (to be run considering there is actual song data
#  inside the corresponding folders)

# parameters for training data
sr_train = 22050
winsize_train = 1
# parameters for testing data
sr_test = 22050 # sampling rate of the song audio file to be tested
winsize_test = 2 # size of window (in seconds) for the division in frames of the audio signal
# predictions are run on each frame
# the class that was predicted the most is chosen as the overall prediction for the whole song

# load all the audio (liked, disliked) and perform feature extraction
ap1 = audio_processing.AudioProcessor(sr_train, winsize_train)
features_liked, features_disliked = ap1.extractAllFeatures()

# train the random regression forest
print("Creating the predictive model...")
mt1 = model_training.ModelTrainer(features_liked, features_disliked, ap1.n_samples_liked, ap1.n_samples_disliked, ap1.winsize_f)
model = mt1.fitRRForest()
print("Model created.")

# load the test song and extract its features
print("Processing test song audio...")
at1 = audio_processing.AudioTester(sr_test, winsize_test)
features_test = at1.extractAllFeatures()
print("Test song processed.")

# run the model for the test song
mtest1 = model_testing.ModelTester(features_test, model)
taste1 = mtest1.predictTaste()
print("DONE! The overall prediction is: ",taste1)
# print(mtest1.results) # see the actual predictions for each frame
