import sklearn
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class ModelTrainer:
    def __init__(self, features_liked, features_disliked, n_samples_liked, n_samples_disliked, winsize):
        self.features = np.concatenate((features_liked, features_disliked))
        
        print("Creating ground truth labels...")
        labels_liked, labels_disliked = self.createLabels(n_samples_liked, n_samples_disliked, winsize)
        self.labels = np.concatenate((labels_liked, labels_disliked))
        print("Labels created.")
        
        self.model = self.fitRRForest()

    def createLabels(self, n_samples_liked, n_samples_disliked, winsize):
        # calculate number of frames in data
        num_windows_liked = int(n_samples_liked/winsize)
        if n_samples_liked % winsize !=0:
            num_windows_liked += 1
        num_windows_disliked = int(n_samples_disliked/winsize)
        if n_samples_disliked % winsize !=0:
            num_windows_disliked += 1

        # create arrays with the corresponding class labels
        labels_liked = ['liked']*num_windows_liked
        labels_disliked = ['disliked']*num_windows_disliked
        return labels_liked, labels_disliked

    def fitRRForest(self):
        # create model
        ntrees = 50
        rf = sklearn.ensemble.RandomForestClassifier(n_estimators = ntrees)

        # train model
        rf.fit(self.features,self.labels)

        return rf
