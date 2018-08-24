# Tastic: a machine learning-based music taste predictor

Could a machine guess if you like a specific song or not, just based on a few example songs that you like or dislike?

Tastic aims to predict your taste about a specific song initially based on 4 example songs: 2 songs you like and 2 songs you don't. With every new song that you provide, Tastic will learn more about your music taste and hopefully become more capable of recognizing patterns on those songs to eventually better predict if you like a certain song or not.

Evidently, due to the very nature of the project, Tastic is by no means guaranteed to provide trustworthy results to the user. Tastic has been created as a personal project and as a basic framework to allow the experimentation on the adequacy of the selected features to be extracted, the diverse types of machine learning methods, and variations of those and their parameters,
specifically within the field of Music Information Retrieval. More particularly, this project started based on a personal interest in the application of machine/deep learning techniques to inherently subjective problems such as this one, and the improvements on their performance from a starting point with a significantly small dataset to a gradually larger one.

## Getting started
### Prerequisites
Tastic makes use of YouTube for selecting and downloading the songs audio data. In order for this to work, your host machine must have ffmpeg installed. In a Debian Linux environment you can directly install it using APT:
```
sudo apt-get install ffmpeg
```
See the ffmpeg documentation to know how to install it in other environments.

### Installing Tastic
It is possible to install the latest version of Tastic as a Python package* using pip. As it is a work in progress, it is strongly recommended to install Tastic inside a virtual environment, for instance with virtualenv:
```
virtualenv tastic
source tastic/bin/activate
```
To install it, run the following command:
```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ tasticgenie
```
Tastic currently supports a command-line interface only. To start it, open a Python terminal (within the folder where you want your songs data to be stored) and execute the following lines:
```
>>> import tasticgenie
>>> from tasticgenie import tastic_cli
>>> tastic_cli.app()
```

_*The current version of the package has been tested on an Ubuntu 18.04 machine with Python 3.6.5 and pip 18.0._

## User guide
The Tastic CLI will display the following menu:

```
---------- TASTIC: a machine learning-based music taste predictor ----------
1. New model
2. Continue model
3. Test current model
4. Delete all data
5. Exit
----------------------------------------------------------------------------
```
When selecting '1. New Model', Tastic will prompt the user to enter several links to YouTube videos of songs they like or dislike. Note that, in order to reduce the effects of overfitting, the chosen YouTube videos should preferably reproduce just the music pieces and not additional scenes with e.g. silence or speech, as it often occurs in official music videos.

After training the model, Tastic will ask for an extra YouTube link to a song for which it will try to predict the music taste of the user. It will display the prediction, and right after it will ask the user to confirm if they liked that song or not. This verification step is performed so as to reuse this data for training depending on the labelling done by the user.

The option '2. Continue model' can be selected when 'liked' and 'disliked' song data has already previously been downloaded. This option allows the user to re-train the model (using the original training data plus the songs used for testing until then) and continue feeding test songs to the model, to see how it performs with additional data. It is important to mention that the implemented random forest does not perform online learning (see [To-Do list](https://github.com/luciaconde/Tastic/blob/master/README.md#to-do-list)), that is, when continuing using a model the previous model is not actually reused but rather a new model is trained with the current downloaded data.

If the user wants to keep using the current (already trained) model, that can be done by selecting '3. Test current model', which will feed test songs to the model without re-training it.

The option '4. Delete all data' allows the user to delete all the 'liked', 'disliked' and 'test' audio files in order to start a completely new model (for instance, for a different user).

## Used libraries

The following third-party libraries have been used to code Tastic:

* [youtube-dl](https://github.com/rg3/youtube-dl) - Used for downloading the songs chosen by the user
* [LibROSA](https://github.com/librosa/librosa) - Used for loading the audio files data and extracting the audio features
* [scikit-learn](https://github.com/scikit-learn/scikit-learn) - Used for generating the predictive model (a random regression forest) 

## To-Do list
* Display the percentage of likeness/dislikeness of the prediction (based on the individual predictions for the analyzed audio windows)
* Implement online learning (for current machine learning model or another one potentially more suitable for it)
* Implement additional machine/deep learning technique
  * Make it selectable for the user, along with the random regression forest 
* Implement simple desktop GUI (or web GUI?)

## Authors

* **Lucía Conde**  - [github profile](https://github.com/luciaconde)

Please feel free to send suggestions and recommendations on improvements or additional functionalities!
