# Thing Namer is a program to name things using markov chains. 
# Written by Jeff Emtman as a benefit for the Patreon supporters of Here Be Monsters Podcast (https://HBMpodcast.com)

######################## IMPORTS #######################

# markovify lets us make the new names. 
import markovify
#if you don't have it, run "pip install markovify" on your command line. 

# time package is needed for pauses
import time

######################## USER VARIABLES #######################
#  - Change these variables as you see fit

# How many results to deliver with each run.
number_of_names = 5

# This is the state size of the markov model.  1 will yield the most wild results.
# For short things like names, I wouldn't recommend anything higher than 3.  2 is default.
normalness = 2

# Max number of characters in any given result. 
max_name_length = 15

# A text file where each entry is on a new line.  Used to train markov model.
raw_text = "baby_names.txt"


######################## FUNCTIONS #######################
# sillyPrint lets output print slowly for dramatic effect.  Used heavily throughout program. 

def sillyPrint(the_input, delay = 0.2):
    output = ""
    for i in range(len(the_input)):
        output += the_input[i]
        print(output, end = "\r")
        
        time.sleep(delay) 


######################## WELCOME THE USER #######################
print('''
 ______ _   Welcome to:          , _                                
(_) |  | |    o                 /|/ \                               
    |  | |        _  _    __,    |   |   __,   _  _  _    _   ,_    
  _ |  |/ \   |  / |/ |  /  |    |   |  /  |  / |/ |/ |  |/  /  |   
 (_/   |   |_/|_/  |  |_/\_/|/   |   |_/\_/|_/  |  |  |_/|__/   |_/ 
                           /|   From Jeff Industries and Fabrication 
©2022, Jeff Emtman.        \|                            Version 1.0
Released 2022-05-04 under an MIT License.  See license.txt for details. 

Thing Namer is a tool for naming things.  It uses a text file to train a 
simple Markov model that can generate new names. It comes with a list of 
baby names from the United States from the last hundred-ish years. You can
alter the code to have it generate from anything you'd like though. 

NOTE: This program needs "Markovify" to run: https://pypi.org/project/markovify/

________________________________________________________________________________

''')
time.sleep(1)


####################### LOADING / PROCESSING / TRAINING MODEL #######################

print("Pre-processing the needed assets.")
time.sleep(1)

# Open the raw text and read it line-by-line, call this "corpus"
print("Loading source: ", raw_text)
with open(raw_text) as f: 
    corpus = f.readlines()

# Markovify wants things separated by spaces, so, iterate through the corpus
# and add a space between each character
space_separated_corpus = ""
for line in corpus: 
    line = " ".join(line)
    space_separated_corpus += line
print("Done.\n")

# Now, build a markovify model from it
print("Building markov model with state size of", normalness)
markov_model = markovify.NewlineText(space_separated_corpus, state_size=normalness)

print("Done.  Ready to name.")



####################### MAIN LOOP #######################
while True: 
    print(" - - - - - - - - - - - - - - \n\n")
    time.sleep(.5)
    thing_to_name = input(str("What would you like to name? eg. dog, plant, baby, etc...\n"))
    
    print("Thank you.  Generating", number_of_names, "names for your", thing_to_name)

    #fake loading bar
    sillyPrint('_.~"~._.~"~._.~"~._.~"~._\n', delay = .2)

    print("\nConsider naming your", thing_to_name,)

    for i in range(number_of_names): 
        # Generate a name uses the 'make_short_sentences' function of markovify which executes pretty much instantly.
        name = str(markov_model.make_short_sentence(max_name_length))

        #combining it into a simple string so sillyPrint can handle it
        output = ("   " + str(i+1) +".  " + name + "\n")

        # sillyprint the output, pause for a moment to read.
        sillyPrint(output, delay=.2)
        time.sleep(2)

    ## Should it run again? 
    run_again = input(str("\nWould you like to run again? (Y/N)"))
    
    if run_again.lower() == "y":
        print("\nRunning again.")
        continue
    else: 
        print("\nThanks for coming by.  Hope it works out for you.")
        print("Exiting.")
        time.sleep(2)
        break 