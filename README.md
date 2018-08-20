# Tastic: a machine learning-based music taste predictor

Could a machine guess if you like a specific song or not, just based on a few example songs that you like or dislike?

Tastic aims to predict your taste about a specific song initially based on 4 example songs: 2 songs you like and 2 songs you don't. With every new song that you provide, Tastic will learn more about your music taste and hopefully become more capable of recognizing patterns on those songs to eventually better predict if you like a certain song or not.

Evidently, due to the very nature of the project, Tastic is by no means guaranteed to provide trustworthy results to the user. Tastic has been created as a personal project and as a basic framework to allow the experimentation on the adequacy of the selected features to be extracted, the diverse types of machine learning methods, and variations of those and their parameters,
specifically within the field of Music Information Retrieval. More particularly, this project started based on a personal interest on the application of machine/deep learning techniques to inherently subjective problems such as this one, and the improvements on their performance from a starting point with a significantly small dataset to a gradually larger one.

## Instructions manual
Tastic currently supports a command-line interface only. To start it, run tastic_cli.py. It will display the following menu:

```
---------- TASTIC: a machine learning-based music taste predictor ----------
1. New model
2. Continue model
3. Delete all data
4. Exit
----------------------------------------------------------------------------
```
When selecting '1. New Model', Tastic will prompt you to enter several links to YouTube videos of songs you like or dislike. Note that, in order to reduce the effects of overfitting, the chosen YouTube videos should preferably reproduce just the music pieces and not additional scenes with e.g. silence or speech, as it often occurs in official music videos.

TBD

### Dependencies

The following third-party libraries -and hence their corresponding dependencies- have been used to code Tastic:

* [youtube-dl](https://github.com/rg3/youtube-dl) - Used for downloading the songs chosen by the user
* [LibROSA](https://github.com/librosa/librosa) - Used for loading the audio files data and extracting the audio features
* [scikit-learn](https://github.com/scikit-learn/scikit-learn) - Used for generating the random regression forest 

## Authors

* **Lucía Conde**  - [github profile](https://github.com/luciaconde)

Please feel free to send suggestions and recommendations on improvements or additional functionalities!
