import audio_processing
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
    print(75 * "-")

#def createModel():
    #--

#def verifyExistingModel():
    #--

#def continueModel():
    #--

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
        # add function
    elif option == 2:
        print(5 * "-", "Continuing model...", 5 * "-")
        # add function
    elif option == 3:
        print(5 * "-", "Deleting all data...", 5 * "-")
        deleteAllData()
    elif option == 4:
        print(5 * "-", "Closing Tastic...", 5 * "-")
        # add function
        app_open = False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong one, we don't have that many options! Please choose another one.")
