#!/usr/bin/env python3
import sys
import random
import string
import colorama
import time
from collections import namedtuple
from datetime import datetime
from pprint import pprint
from readchar import readchar, key


Input = namedtuple('Input', ['requested', 'received', 'duration'])
input_list = []


dict = {}
    
def main(): 
    if sys.argv[1] == "-mv":
        mvmode(sys.argv[2])
        pprint(dict)
    elif sys.argv[1] == "-utm":
        utmode(sys.argv[2])
        pprint(dict)
    elif sys.argv[1] == "-h":
        helpmsg()
         
    else:
        print("Invalid input")

def mvmode(max_number):
    n_correct = 0
    n_wrong = 0
    time_correct = 0
    time_wrong = 0
    dict['test_start'] = time.asctime()
    for i in range(0,int(max_number)):
        start_time = time.time()
        n = random.choice(string.ascii_lowercase)
        print("Type letter " + colorama.Fore.BLUE + str(n)+ colorama.Style.RESET_ALL)
        input_char = readchar()
        if input_char == key.SPACE:
            break
        if n == input_char :
            print("You typed letter "+ colorama.Fore.GREEN + input_char+colorama.Style.RESET_ALL)
            n_correct += 1
            time_correct += time.time() - start_time
        else :
            print("You typed letter "+ colorama.Fore.RED + input_char+colorama.Style.RESET_ALL)
            n_wrong += 1
            time_wrong += time.time() - start_time

        input_list.append(Input(n, input_char, time.time() - start_time))


    dict['inputs'] = input_list
    if n_correct != 0 or n_wrong != 0:
        dict['accurary'] = n_correct / (n_correct + n_wrong)
    else:
        dict['accurary'] = 0
    dict['number_of_hits'] = n_correct
    dict['number_of_types'] = n_correct + n_wrong
    dict['test_end'] = time.asctime()
    if len(dict['inputs']) > 0:
        dict['test_duration'] = sum([x.duration for x in dict['inputs']])
        dict['type_average_duration'] = sum([x.duration for x in dict['inputs']]) / len(dict['inputs'])
    else:
        dict['type_average_duration'] = 0
        dict['test_duration'] = 0
    # if statmet to avoid division by zero
    if n_correct != 0:
        dict['type_hit_average_duration'] = time_correct / n_correct
    else :
        dict['type_hit_average_duration'] = 0
    if n_wrong != 0:
        dict['type_miss_average_duration'] = time_wrong / n_wrong
    else:        
        dict['type_miss_average_duration'] = 0




def utmode(max_time):
    n_correct = 0
    n_wrong = 0
    time_correct = 0
    time_wrong = 0
    mode_start_time = time.time()
    while time.time() < mode_start_time + int(max_time):
        start_time = time.time()
        n = random.choice(string.ascii_lowercase)
        print("Type letter " + colorama.Fore.BLUE + str(n)+ colorama.Style.RESET_ALL)
        input_char = readchar()
        if input_char == key.SPACE:
            break
        if n == input_char :
            print("You typed letter "+ colorama.Fore.GREEN + input_char+colorama.Style.RESET_ALL)
            n_correct += 1
            time_correct += time.time() - start_time
        else:
            print("You typed letter "+ colorama.Fore.RED + input_char+colorama.Style.RESET_ALL)
            n_wrong += 1
            time_wrong += time.time() - start_time

        input_list.append(Input(n, input_char, time.time() - start_time))

    dict['inputs'] = input_list
    if n_correct != 0:
        dict['accurary'] = n_correct / (n_correct + n_wrong)
    else:
        dict['accurary'] = 0
    dict['number_of_hits'] = n_correct
    dict['number_of_types'] = n_correct + n_wrong
    dict['test_duration'] = sum([x.duration for x in dict['inputs']])
    dict['test_end'] = time.asctime()
    dict['test_start'] = mode_start_time
    if len(dict['inputs']) > 0:
        dict['type_average_duration'] = sum([x.duration for x in dict['inputs']]) / len(dict['inputs'])
    else:
        dict['type_average_duration'] = 0
    if n_correct != 0:
        dict['type_hit_average_duration'] = time_correct / n_correct
    else :
        dict['type_hit_average_duration'] = 0
    if n_wrong != 0:
        dict['type_miss_average_duration'] = time_wrong / n_wrong
    else:        
        dict['type_miss_average_duration'] = 0

def helpmsg():
    msg="""
    usage: main.py [-h] [-utm] [-mv MAX_VALUE]

Definition of test mode

optional arguments:
  -h, --help            show this help message and exit

  -utm, --use_time_mode
                        Max number of secs for time mode or maximum number of inputs for number of inputs mode.

  -mv MAX_VALUE, --max_value MAX_VALUE
                        Max number of seconds for time mode or maximum number of inputs for number of inputs mode."""
    print(msg)
            



if __name__ == "__main__":
    main()