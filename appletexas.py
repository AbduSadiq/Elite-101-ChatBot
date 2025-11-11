import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

import textblob
from textblob import download_corpora
try:
    textblob.download_corpora.download_all()
except:
    pass

from nrclex import NRCLex
import uuid

print("Welcome to Apple's customer service for their Texas branch. I am your virtual assistant Alex, before we begin, I will just be needing some information.")
input("Press enter to continue...")

# Asks customer name.

name = input("Please enter your name: ")

print("Great, " + name + ", what will you be needing help with today? ")

# Replies wiht greeting after entering name.

while True:
    print("Choose an option #! ")
    print("1) Start a return.")
    print("2) Start an exchange.")
    print("3) Following up about an existing purchase.")
    print("4) Exit chat")

# Allows me to choose an option.

    choice = input("Make a choice please: ") 
    emotion = NRCLex(choice)
    top_emotion = emotion.top_emotions
    if top_emotion:
        print(f"(Alex detects your emotion as: {top_emotion[0][0]})")  
    choice = choice.strip()

# Detects the emotion.

    if choice == '1':
        input("Looks like you want to start a return, may I have your order number. ")

        city = input("Great, Now please enter your city: ")

        cityCase = city.title()    

        city_emotion = NRCLex(city)
        top_city_emotion = city_emotion.top_emotions
        if top_city_emotion:
            print(f"(Alex detects your emotion as: {top_city_emotion[0][0]})")
   
# Prints the top emotion exhibited and shown.

        stores_in_cities = {
            "Austin": ["Domain (Northside)", "Barton Creek"],
            "Dallas": ["NorthPark Center", "Knox Street", "Galleria Dallas" ],
            "Houston": ["Memorial City", "Houston Galleria", "Willowbrook Mall", "Highland Village"],
            "El Paso": ["Cielo Vista Mall"],
            "Fort Worth": ["University Park Village"],
            "Friendswood": ["Baybrook"],
            "San Antonio": ["North Star", "La Cantera"],
            "Southlake": ["Southlake Town Square"],
            "Sugar Land": ["First Colony Mall"],
            "The Woodlands": ["The Woodlands"]
        }

        if city in stores_in_cities:
            print("Here are the stores available for " + city + ".")
            for store in stores_in_cities[city]:
                print("-" + store)
        else:
            print("Invalid city, please try again.")

        input("Press enter to continue...")

        print("Alright, I have provided you with a return ID below which you will enter at the location closest to you in your city. Return ID:", uuid.uuid4())
        print("Have a great day, Goodbye")
        break
        
    elif choice == '2':
        orderNumber = input("Looks like you want to start an exchange, may I have your order number. ")

        print("Here is what I found for " + orderNumber)

        city = input("Great, Now please enter your city: ")

        cityCase = city.title()  

        stores_in_cities = {
            "Austin": ["Domain (Northside)", "Barton Creek"],
            "Dallas": ["NorthPark Center", "Knox Street", "Galleria Dallas" ],
            "Houston": ["Memorial City", "Houston Galleria", "Willowbrook Mall", "Highland Village"],
            "El Paso": ["Cielo Vista Mall"],
            "Fort Worth": ["University Park Village"],
            "Friendswood": ["Baybrook"],
            "San Antonio": ["North Star", "La Cantera"],
            "Southlake": ["Southlake Town Square"],
            "Sugar Land": ["First Colony Mall"],
            "The Woodlands": ["The Woodlands"]
        }

# Gives a list of cities to choose from as this is the Texas branch and these cities will only be in Texas.
        
        if city in stores_in_cities:
            print("Here are the stores available for " + city + ".")
            for store in stores_in_cities[city]:
                print("-" + store)
        else:
            print("Invalid city, please try again.")

        input("Press enter to continue...")

        print("Alright, I have provided you with a return ID below which you will enter at the location closest to you in your city. Return ID:", uuid.uuid4())
        print("Have a great day, Goodbye")
        break

# Ends the exchange choice and segment of the code. 

    elif choice == '3':
        orderNumber = input("Looks like you want to follow up for an existing order, may I have your order number.")

        print("Perfect, your order is currently being processed at out facility and will be sent out for delivery shortly")

        break

# Follows up the current location of the order.
    
    elif choice == '4':
        print("Have a great day, Goodbye")
        break

# Allows for the exit of this program.

    else:
        print("Choice not valid, please try again later.")
