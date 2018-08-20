# Tastic: a machine learning-based music taste predictor

Could a machine guess if you like a specific song or not, just based on a few example songs that you like or dislike?

Tastic aims to predict your taste about a specific song initially based on 4 example songs: 2 songs you like and 2 songs you don't. With every new song that you provide, Tastic will learn more about your music taste and hopefully become more capable of recognizing patterns on those songs to eventually better predict if you like a certain song or not.

Evidently, due to the very nature of the project, Tastic is by no means guaranteed to provide trustworthy results to the user. Tastic has been created as a personal project and as a basic framework to allow the experimentation on the adequacy of the selected features to be extracted, the diverse types of machine learning methods, and variations of those and their parameters,
specifically within the field of Music Information Retrieval. More particularly, this project started based on a personal interest in the application of machine/deep learning techniques to inherently subjective problems such as this one, and the improvements on their performance from a starting point with a significantly small dataset to a gradually larger one.

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
When selecting '1. New Model', Tastic will prompt the user to enter several links to YouTube videos of songs they like or dislike. Note that, in order to reduce the effects of overfitting, the chosen YouTube videos should preferably reproduce just the music pieces and not additional scenes with e.g. silence or speech, as it often occurs in official music videos.

After training the model, Tastic will ask for an extra YouTube link to a song for which it will try to predict the music taste of the user. It will display the prediction, and right after it will ask the user to confirm if they liked that song or not. This verification step is performed so as to reuse this data for training depending on the labelling done by the user.

The option '2. Continue model' can be selected when 'liked' and 'disliked' song data has already previously been downloaded. This option allows the user to continue feeding test songs to the model and see how it performs with additional data. It is important to mention that the implemented random forest does not perform online learning (see section 'To-Do list' below), that is, when continuing using a model the previous model is not actually reused but rather a new model is trained with the current downloaded data.

The option '3. Delete all data' allows the user to delete all the 'liked', 'disliked' and 'test' audio files in order to start a completely new model (for instance, for a different user).

### Dependencies

The following third-party libraries -and hence their corresponding dependencies- have been used to code Tastic and must therefore be installed in order to run it:

* [youtube-dl](https://github.com/rg3/youtube-dl) - Used for downloading the songs chosen by the user
* [LibROSA](https://github.com/librosa/librosa) - Used for loading the audio files data and extracting the audio features
* [scikit-learn](https://github.com/scikit-learn/scikit-learn) - Used for generating the random regression forest 

## To-Do list
* Implement simple desktop GUI
* Implement online learning (for current machine learning model or another one potentially more suitable for it)
* Implement additional machine/deep learning technique
  * Make it selectable for the user, along with the random regression forest 
* Implement web GUI?

## Authors

* **Lucía Conde**  - [github profile](https://github.com/luciaconde)

Please feel free to send suggestions and recommendations on improvements or additional functionalities!
