"Oh hi didn't see you there, my name is avery!"

keepplaying = 'yes'
print('start')
while keepplaying == 'yes' or keepplaying == 'Yes':
    userChoice = input("I'm lost can you help me get out?")
    if userChoice == 'yes' or userChoice == 'Yes':
        keepplaying = 'no'
    elif userChoice == "no" or userChoice == "No":
        print("aww okay I guess I'll figure it out on my own. Bye!")
        keepplaying = input("would you like to try again? ")
        if keepplaying == 'no':
            quit()

keepplaying = 'yes'
while keepplaying == 'yes' or keepplaying == 'Yes':
    southnorthchoice = input("should I go north or south?")
    if southnorthchoice == "South" or southnorthchoice == 'south':
        print("okay well now that I'm here where should I go?")
        print("Hannah: Oh finally another civilian, where are you heading to?")
        print("Avery: I'm heading to 500 paula for girls who code")
        print("Hannah: Omg me too! Is your teacher Mr. Maxwell?!")
        print("Avery: Yes!")
        keepplaying = "no"
    elif southnorthchoice == 'North' or southnorthchoice == 'north':
        print("friendly bear: you seem lost do you need help?")
        print("avery: actually I have a friend helping she told me to go north to get to 500 paula ave.")
        print("friendly bear: oh no your supposed to go south to get to 500 paula ave ")
        print("avery: ahh okay thank you!")
        exit()
    
    
    

            
