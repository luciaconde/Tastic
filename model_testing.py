import sklearn
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from statistics import mode
import shutil

class ModelTester:
    def __init__(self, features, model, song_title):
        self.results = model.predict(features)
        self.taste = 'none'
        self.title = song_title

    def predictTaste(self):
        try:
            self.taste = mode(self.results)
        except StatisticsError: # if the number of 'liked' predictions equals the number of 'disliked' predictions,
            self.taste = 'dislike' # tag the whole song as disliked (due to the big discord among predictions)

        return self.taste

    def verifyPrediction(self, true_taste):
        # reuse the testing data as training data for the next model
        shutil.move("tastic_data/test/" + self.title, "tastic_data/" + true_taste + "/" + self.title)

    
