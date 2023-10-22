# Turingmachine-Simulator

## 1. How to run it

If you want to run the Turingmachine-simulator the easiest way is to do it over the command-line.

To run it simply enter a command in the form of: "python main.py 'filename' 'input_word'".

In this case 'filename' and 'input_word' are mandatory and the program will not run if they are missing.
1. filename is the name of the file that contains the TM-specification. Please put the file into the same directory as the main.py and this readme.MD
2. input_word is the word you want to run the TM with. Make sure the input_word only contains symbols from the input_alphabet you specified in the TM-file

Now just run the command and the strings on what the TM is doing in each step will be printed out. (TM-file and input_word have to be syntactically correct)

## 2. Explanation of the Simulation

Basically we have 2 parts to the simulation:

1.Read through the file with the TM-specification and save them in our TM-model.

2.Calculate the outcome of the TM with the given input_word and print out the current status of the TM-tape.

1. Regarding the first part, we simply scrap through the file and take all the important information. We then save this information inside our TuringMachineModel. This is the class that later on will also be tasked to actually calculate on the given input_word. We also use two extra classes to save more specific state-information. This is mainly to make it easier to find the specifics of what to do next.
2. Regarding how we run the TM. We first instanciate the TM in the "main.py"-file. There we also take care of the input_word and filename. After scrapping the file for all the necessary information we then go ahead and run our TM with the function 'run_machine' in the class TuringMachineModel. The idea is that we can look at the string as if it were a list (in python list, other languages would use an array). This is why we can simply use one integer to keep track of where we are at in the input-string. Now we simply read the symbol of the position we are and then use the information we scrapped earlier to find out what we have to do next. This will be repeated until the current_state is the same as the ending_state were we then output the current string one final time and then end the simulation. We also have to simulate the infinite length of the tape. Technically we do not need an infinite amount of space, but we can simulate this by adding 'BBB' to each side of the string. Whenever one of those 'B's gets overwritten we simply replace it with a new one. This way we always have at least 'BBB' on each side of the string and therefore we simulate the infinite length of the turing-tape.

## 3. Files not directly important for the simulation of the TM

The following files do not have much to do with the simulation itself and can be ignored for explanation-purposes.
Those files are:
1. helper_modules/argument_parser.py := This file simply reads the inputs 'filename' and 'input_word' from the command-line and doesn't really do anything with the TM-simulation.
2. errors/tm_errors := Defines the error for when an input-word contains a symbol that is not within the input-alphabet.


## 4. Regarding '.TM'-files

The '.TM'-files specify the properties of given Turing-machines.
1. invert.TM is a file that was given to us. It can be used to test the workings of our TM-simulator. invert.TM simply defines a Turing-machine that inverts a given binary number.

Specifications to calculate something with this TM:

filename = invert.TM

input_word = a string of '0' and '1'


2. add_two_binaries.TM is a file created by our team. It can be used to add two binary numbers together.

Specifications to calculate something with this TM:

filename = add_two_binaries.TM

input_word = a string of '0' and '1'. The two numbers you want to add together have to be seperated by a '#'