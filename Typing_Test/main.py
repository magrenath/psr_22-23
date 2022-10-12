import argparse
from colorama import Fore, Back, Style
from readchar import readkey
import random
import string
import time
from collections import namedtuple

Inputs = namedtuple('Input', ['requested', 'received','duration'])
init = time.time()
my_dict = {}

# Point 2: receives input arguments that will define the game mode
def initValues():
    
    parser = argparse.ArgumentParser(description = 'Definition of test mode.')
    parser.add_argument('-utm', '--use_time_mode', type=int,
                    help="Max number of secs for time mode or maximum number of inputs for number of inputs mode.")
    parser.add_argument('-mv', '--max_value', type=int,
                    help="Max number of secs for time mode or maximum number of inputs for number of inputs mode.")

    # creates dictionary
    args = vars(parser.parse_args())
    # assings a variable to the corresponding input values
    maxv = args["max_value"]
    temp = args["use_time_mode"]

    # defines game mode
    if maxv == None:
        print("User Time Mode: you have " + str(temp) + " seconds!")
        return{"use_time" : temp}
    else:
        print(Fore.BLUE + "Maximum Input Mode: you have " + str(maxv) + " chances" + Style.RESET_ALL)
        return{"maximum_input" : maxv}


# Point 3: ask to press a letter to start
def startGame():
    print(Fore.YELLOW + "Press any key to start the game:" + Style.RESET_ALL)
    initialize = readkey()
    if initialize != None:
        return True


# Point 4: show a random lowercase letter and receive answer
def askLetter():
    asked_letter = random.choice(string.ascii_letters).lower()
    print("Press " + asked_letter)
    return asked_letter
def answLetter():
    inserted_letter = readkey()
    return inserted_letter


# Point 5: distinct game modes
def modeSelection():

    input = initValues()
    mode = list(input.keys())[0]

    return mode

# Point 5.1: User Time Mode
def gameTime(t):
    types = []
    type_average_duration = []
    type_hit_average_duration = []
    type_miss_average_duration = []
    
    number_of_types = 0
    number_of_hits = 0

    time_init = time.time()
    delta = 0

    while delta < t:
        time_request = time.time()
        requested = askLetter()
        received = answLetter()

        if requested == received:
            time_hit_answ = time.time()
            print(Fore.GREEN + "You typed " + received + Style.RESET_ALL)
            number_of_hits += 1
            number_of_types += 1
            delta_hit_answ = time_hit_answ - time_request
            type_hit_average_duration.append(delta_hit_answ)
        else:
            time_miss_answ = time.time()
            print(Fore.RED + "You typed " + received + Style.RESET_ALL)
            number_of_types +=1
            delta_miss_answ = time_miss_answ - time_request
            type_miss_average_duration.append(delta_miss_answ)
        
        time_f = time.time()
        delta1 = time_f - time_request
        type_average_duration.append(delta1)
        types.append(Inputs(requested, received, delta1))

        time_end = time.time()
        delta = time_end - time_init
            
        if received == " ":
            break

    dictionary(types, delta, type_average_duration, number_of_hits, number_of_types, type_hit_average_duration, type_miss_average_duration)
    return

# Point 5.2: Maximum Input Mode
def maxInput(m):
    types = []
    type_average_duration = []
    type_hit_average_duration = []
    type_miss_average_duration = []

    number_of_types = 0
    number_of_hits = 0

    time_init = time.time()
    delta = 0

    for n in range(0, m):
        time_request = time.time()
        requested = askLetter()
        received = answLetter()
        

        if requested == received:
            time_hit_answ = time.time()
            print("You typed " + Fore.GREEN + received + Style.RESET_ALL)
            number_of_hits += 1
            number_of_types += 1
            delta_hit_answ = time_hit_answ - time_request
            type_hit_average_duration.append(delta_hit_answ)
        else:
            time_miss_answ = time.time()
            print("You typed " + Fore.RED + received + Style.RESET_ALL)
            number_of_types +=1
            delta_miss_answ = time_miss_answ - time_request
            type_miss_average_duration.append(delta_miss_answ)

        time_f = time.time()
        delta1 = time_f - time_request
        type_average_duration.append(delta1)
        types.append(Inputs(requested, received, delta1))

        time_end = time.time()
        delta = time_end - time_init

        if received == " ":
            break
        
    dictionary(types, delta, type_average_duration, number_of_hits, number_of_types, type_hit_average_duration, type_miss_average_duration)
    return
  
def dictionary(types, delta, type_average_duration, number_of_hits, number_of_types, type_hit_average_duration, type_miss_average_duration):


    seconds = time.time()
    end_time = time.ctime(seconds)
    accuracy = number_of_hits/number_of_types
    
    if sum(type_hit_average_duration) == 0:
        typehit_average_duration = 0
    else:
        typehit_average_duration = sum(type_hit_average_duration)/len(type_hit_average_duration)
    
    if sum(type_miss_average_duration) == 0:
        typemiss_average_duration = 0
    else:
        typemiss_average_duration = sum(type_average_duration)/len(type_miss_average_duration)

    if sum(type_average_duration) == 0:
        type_averageduration = 0
    else:
        type_averageduration = sum(type_average_duration)/len(type_average_duration)    

    my_dict['test_end'] = end_time
    my_dict['test_duration'] = delta
    my_dict['inputs'] = types
    my_dict['number_of_types'] = number_of_types
    my_dict['number_of_hits'] = number_of_hits
    my_dict['accuracy'] = accuracy
    my_dict['type_average_duration'] = type_averageduration
    my_dict['type_hit_average_duration'] = typehit_average_duration
    my_dict['type_miss_average_duration']= typemiss_average_duration
    
    print(my_dict)

    return

def main():
    
    input_values = initValues()
    startGame()
    
    mode = modeSelection()
    if mode == "use_time":
        gameTime(input_values["use_time"])
    else:
        maxInput(input_values["maximum_input"])

if __name__ == "__main__":
    main()