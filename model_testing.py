import sklearn
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from statistics import mode

class ModelTester:
    def __init__(self, features, model):
        self.results = model.predict(features)

    def predictTaste(self):
        taste = 'dk'
        try:
            taste = mode(self.results)
        except StatisticsError: # if the number of 'liked' predictions equals the number of 'disliked' predictions,
            taste = 'disliked' # tag the whole song as disliked (due to the big discord among predictions)

        return taste

    
