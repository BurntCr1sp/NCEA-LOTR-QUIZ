import time # Imports time to be used later in the code
import os # Imports os to be used later in the code

# The questions, options to awnser and awnsers for the quiz all put in lists
questions = [1,"Who possesses the ring of power at the start of the trilogy?",2,"Who do the hobbits encounter at the Prancing Pony?",3,"How many members make up the fellowship of the ring?",4,"What is the name of the elf in the fellowship?",5,"What is the name of the dwarf in the fellowship?",6,"Who is the first member of the fellowship to be separated from the group?",7,"What happens at the end of the first movie?",8,"Where is Sarumans tower, Orthanc, located?",9,"Who has been following Sam and Frodo?",10,"Who is the king of Rohan?"] 
options = [1,"A. Bilbo B. John C. Dumbledoor D. Humblemoore E. stewie griffin",2,"A. The manager of the store B. Their cousin C. A prancing pony D. Legoland E. Strider",3,"A. 1.5 B. 10 C. enough D. 9 E. 7",4,"A. Buddy B. Legolas C. Jolly D. Bernard E. Aegnor",5,"A. Peter Dinklage B.Tommy Morrison C. Gimli D. Balin E. Dwalin",6,"A. Gandalf B. Jerry the stone C. The ring D. Frodo E. Aragorn",7,"A. Merry and Pippin are carried off by orcs and Uruk-hai B. Boromir is killed C. Frodo and Sam leave the others behind D. All of the above",8,"A. Minas Tirith B. Rivendell C. Isengard D. Helms Deep E. Next to his grandmas house",9,"A. Gollum B. Sméagol C. A and B D. None of the above E. Max Verstappen",10,"A. Wormtongue B. Éowyn C. Éomer D. Sméagol E. Théoden"]
awnsers = [1,"A",2,"E",3,"D",4,"B",5,"C",6,"A",7,"D",8,"C",9,"A",10,"E"]

def question1(): # This function controls the first question and all its options & awnsers
    print(questions[1])
    print('')
    print(options[1])
    print('')
    Q1 = input('Your awnser: ')
    if Q1 == awnsers[1]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[1])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def question2(): # This function controls the second question and all its options & awnsers
    print(questions[3])
    print('')
    print(options[3])
    print('')
    Q2 = input('your awnser: ')
    if Q2 == awnsers[3]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[3])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def question3(): # This function controls the third question and all its options & awnsers
    print(questions[5])
    print('')
    print(options[5])
    print('')
    Q3 = input('your awnser: ')
    if Q3 == awnsers[5]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[5])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def question4(): # This function controls the fourth question and all its options & awnsers
    print(questions[7])
    print('')
    print(options[7])
    print('')
    Q4 = input('your awnser: ')
    if Q4 == awnsers[7]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[7])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def question5(): # This function controls the fifth question and all its options & awnsers
    print(questions[9])
    print('')
    print(options[9])
    print('')
    Q5 = input('your awnser: ')
    if Q5 == awnsers[9]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[9])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def question6(): # This function controls the sixth question and all its options & awnsers
    print(questions[11])
    print('')
    print(options[11])
    print('')
    Q6 = input('your awnser: ')
    if Q6 == awnsers[11]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[11])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def question7(): # This function controls the seventh question and all its options & awnsers
    print(questions[13])
    print('')
    print(options[13])
    print('')
    Q3 = input('your awnser: ')
    if Q3 == awnsers[13]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[13])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def question8(): # This function controls the eighth question and all its options & awnsers
    print(questions[15])
    print('')
    print(options[15])
    print('')
    Q4 = input('your awnser: ')
    if Q4 == awnsers[15]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[15])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def question9(): # This function controls the ninth question and all its options & awnsers
    print(questions[17])
    print('')
    print(options[17])
    print('')
    Q5 = input('your awnser: ')
    if Q5 == awnsers[17]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[17])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def question10(): # This function controls the tenth question and all its options & awnsers
    print(questions[19])
    print('')
    print(options[19])
    print('')
    Q6 = input('your awnser: ')
    if Q6 == awnsers[19]:
        print('Correct')
    else:
        print('Incorrect, the awnser was', awnsers[19])
    time.sleep(4) # Makes the program wait 4 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def startQ2(): # This function controls the starting question 2

    startQ2 = input('Type "the any key" to start: ')
    print('')

    if startQ2 == 'the any key':
        print('Good job, your are one of the people who read it right... thank you...')
        print('')
        time.sleep(3)
        print('Please awnser in caps... other than that lets begin')
        print('')
        time.sleep(3)
        os.system('clear')
    else:
        print('You should have typed "the any key".... your no fun...')
        print('')
        time.sleep(3)
        print('Oh well... please awnser in caps... other than that lets begin')
        print('')
        time.sleep(3)# Makes the program wait 3 seconds before continuing to run
    os.system('clear') # Clears the terminal which helps to seperate questions and make things look less messy

def end(): # This function controls the ending to see if the user would like to start over

    end = True
    
    again = input("Would you like to play again? ").lower()

    while end == True:
        if again == "yes":
            amountQ1() # goes to the amountQ1 function to follow its code
        if again == "no":
            exit() # Exits and ends the program
        again = input("Would you like to play again? ").lower()

def amountQ1(): # This function controls when and where everything is in the order

    amountQ1 = True
    
    user_num = input("Would you like 6 questions or 10? ")

    while amountQ1 == True:
        if user_num == "6": # goes to and follows the code in those fuctions only if the user enters 6
            startQ2()
            question1() 
            question2()
            question3()
            question4()
            question5()
            question6()
            end()
        if user_num == "10": # goes to and follows the code in those fuctions only if the user enters 10
            startQ2()
            question1()
            question2()
            question3()
            question4()
            question5()
            question6()
            question7()
            question8()
            question9()
            question10()
            end()
        user_num = input("Would you like 6 questions or 10? ")

print('Welcome to the lord of the rings quiz, this quiz will test you and your knowledge of the lord of the rings. But first...')
time.sleep(3) # pauses the code for 3 seconds before moving on
amountQ1() # Goes to and follows the rules of this function (amountQ1)


