from sys import exit
import random
 
countries = [['India', 'New Delhi'], ['United States of America', 'New York'], ['Afghanistan', 'Kabul'], ['Australia', 'Canberra'], ['Austria', 'Vienna'], ['Cambodia', 'Phnom Penh']]
 
countries_answered = []
 
def get_random_country_and_capital():
    randint = random.randint(0, countryCount-1)
    country = countries[randint][0]
    capital = countries[randint][1]
    while(country in countries_answered):
        randint = random.randint(0, countryCount-1)
        country = countries[randint][0]
        capital = countries[randint][1]
    return country, capital
    
 
if __name__ == "__main__":
    points = 0    
    print "Hello and welcome to the travel game"
    countryCount = len(countries)
    print "Our world has %r countries" % countryCount
    start = raw_input("Are you ready to start the game ? (yes|no)")
    if start == "no":
        print "Goodbye !"
        exit(0)
    else:
        # Start the game        
        name = raw_input("What is your name ? ")
        print "Fasten your seat belt %s we are getting started ! If you want to quit midway, press CTRL-C" % name
        while(True):
            country, capital = get_random_country_and_capital()
            print "You have landed in %s" % country
            print "The immigration officer wants to find out if you know the capital of %s" % country
            answer = raw_input("Please type the capital of %s : " % country)
            if answer.lower() == capital.lower():
                points += 1
                countries_answered.append(country)
                print "Awesome! That is absolutely right"
                print "Your current score is %d" % points
                if(points == countryCount):
                    print "You have earned the maximum points in this game. We hope you enjoyed playing it"
                    exit(0)
            else:
                print "Sorry that is the wrong answer!" 
                