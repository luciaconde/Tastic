# Tastic: a machine learning-based music taste predictor

Could a machine guess if you like a specific song or not, just based on a few example songs that you like or dislike?

Tastic aims to predict your taste about a specific song initially based on 4 example songs: 2 songs you like and 2 songs you don't. With every new song that you provide, Tastic will learn more about your music taste and hopefully become more capable of recognizing patterns on those songs to eventually better predict if you like a certain song or not.

Evidently, due to the very nature of the project, Tastic is by no means guaranteed to provide trustworthy results to the user. Tastic has been created as a personal project and as a basic framework to allow the experimentation on the adequacy of the selected features to be extracted, the diverse types of machine learning methods, and variations of those and their parameters,
specifically within the field of Music Information Retrieval.

## Instructions manual
(placeholder for instructions on the TBD UI)

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

### Dependencies

The following third-party libraries -and hence their corresponding dependencies- have been used to code Tastic:

* [youtube-dl](https://github.com/rg3/youtube-dl) - Used for downloading the songs chosen by the user
* [LibROSA](https://github.com/librosa/librosa) - Used for loading the audio files data and extracting the audio features
* [scikit-learn](https://github.com/scikit-learn/scikit-learn) - Used for generating the random regression forest 

## Authors

* **Lucía Conde**  - [github profile](https://github.com/luciaconde)

See the list of [contributors](https://github.com/luciaconde/Tastic/graphs/contributors).
