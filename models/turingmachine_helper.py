from typing import Dict, List

from models.state_function_model import StateFunctionModel, FunctionDescrModel

def _read_state_functions(remaining_file_lines: List[str]) -> Dict[int, StateFunctionModel]:
    """
    :remaining_file_lines: All the lines within the .TM-file that are concerned with describing the TMs behavior
    """

    # We first need to get rid of all the '\n' in the file-lines
    stripped_lines = list(map(lambda x: x.replace("\n", ""), remaining_file_lines))

    state_descr_dict = {}
    for line in stripped_lines:
        # For every state we create a new entry in the dictionary
        if int(line[0]) not in list(state_descr_dict.keys()):
            state_descr_dict[int(line[0])] = []
        
        # Now we take the information from the document and put it into the dict
        state_descr = [char for char in line.split(' ')]
        state_descr_dict[int(state_descr[0])].append(state_descr[1:])

    # Now we technically have all the information we need in order
    # To access the information better later on we use classes and reorder it in a better way.
    state_function_models = {}
    for state, input_list in state_descr_dict.items():
        all_function_descr = {}

        for inputtable in input_list:
            function_descr = FunctionDescrModel(
                input_symbol=inputtable[0],
                next_state=int(inputtable[1]),
                symbol_to_write=inputtable[2],
                direction=inputtable[3]
            )
            all_function_descr[inputtable[0]] = function_descr

        state_function_models[int(state)] = StateFunctionModel(int(state), all_function_descr)
    
    return state_function_models
    

def read_tm_file(filename) -> Dict:
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Because the linebreak '\n' is always the last char of the list we will not include it in the list
        # we use list comprehension to read the alphabets and put it into a list
        input_alphabet = [char for char in lines[1]][:-1]
        tape_alphabet = [char for char in lines[2]][:-1]

        # Now we can simply read the next to lines to get starting/ending state
        starting_state = int(lines[3])
        ending_state = int(lines[4])

        # The rest of the lines descripe how the states behave, we use a seperate function to extract that information
        state_functions = _read_state_functions(lines[5:])

    return {
        "input_alphabet": input_alphabet,
        "tape_alphabet": tape_alphabet,
        "starting_state": starting_state,
        "ending_state": ending_state,
        "state_functions": state_functions,
    }