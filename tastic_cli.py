import tastic_options

opt = tastic_options.options(22050, 22050, 2, 1)

def menu():
    print(10 * "-", "TASTIC: a machine learning-based music taste predictor", 10 * "-")
    print("1. New model")
    print("2. Continue model")
    print("3. Test current model")
    print("4. Delete all data")
    print("5. Exit")
    print(76 * "-")

def app():
    app_open = True      
  
    while app_open:
        menu()    # display menu
        option = int(input("Enter your choice [1-5]: "))
     
        if option == 1:     
            print(5 * "-", "Creating new model...", 5 * "-")
            opt.createNewModel()
        elif option == 2:
            print(5 * "-", "Continuing model...", 5 * "-")
            opt.continueModel()
        elif option == 3:
            print(5 * "-", "Testing model...", 5 * "-")
            opt.testModel()
        elif option == 4:
            print(5 * "-", "Deleting all data...", 5 * "-")
            opt.deleteAllData()
        elif option == 5:
            print(5 * "-", "Closing Tastic...", 5 * "-")
            app_open = False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong one, we don't have that many options! Please choose another one.")
