import models.turingmachine_helper as tm_helper
from errors.tm_errors import InputNotInAlphabet

from typing import Tuple, Union

class TuringMachineModel():

    def __init__(self, filename):
        # Here we include all attributes (members) of a turing machine
        # We first read the given tm_file with a different function
        tm_modulations = tm_helper.read_tm_file(filename)
        
        self.input_alphabet = tm_modulations["input_alphabet"] # type = List[str]
        self.tape_alphabet = tm_modulations["tape_alphabet"] # type = List[str]
        self.starting_state = tm_modulations["starting_state"] # type = int
        self.ending_state = tm_modulations["ending_state"] # type = int
        self.current_state = tm_modulations["starting_state"] # type = int
        self.state_functions = tm_modulations["state_functions"] # type = Dict[int, StateFunctionModel]

    def _check_input_match_alphabet(self, input: str) -> bool:
        """
        :input: The word you want to give to the turingmachine, to calculate the results.
        
        We simply check if all characters of the input are within the input-alphabet    
        """
        for char in input:
            if char not in self.input_alphabet:
                return False

        return True

    @staticmethod
    def _prepare_word_for_calculation(input: str) -> str:
        """
        :input: The word you want to give to the turingmachine, to calculate the results.

        We simply add 'B's at the ends of the word and some ...
        """
        return f"...B{input}B..."

    @staticmethod
    def _create_printable(preparred_input: str, current_state: int, current_head_position: int) -> str:
        """
        :preparred_input: input-word with the added '...B' on both sides
        
        :current_state: The state the TM currently is in.

        :current_head_position: The position the head-currently is on, related to the preparred_input-str

        Here we create the string, that shows the current string of the TM-tape.
        """
        return f"{preparred_input[0:current_head_position]}[{current_state}]{preparred_input[current_head_position:]}"

    def _calculate_step(self, current_state: int, input_red: str) -> Tuple[Union[int, str]]:
        """
        :current_state: The current state we are in with our TM.

        :input_red: The symbol that we read at the current head-position
        
        We simply calculate what we need to do in the next step.
        """
        function_descr = self.state_functions[current_state].all_function_descr[input_red]
        
        return (function_descr.next_state, function_descr.symbol_to_write, function_descr.direction)

    @staticmethod
    def _replace_string(preparred_input: str, current_head_position: int, new_char: str):
        """
        :preparred_input: input-word with the added '...B' on both sides

        :current_head_position: The position the head-currently is on, related to the preparred_input-str

        :new_char: The symbol we need to write in the current_head_position

        Because strings are immutable in python we need to write a specific function to change the one symbol in the current_head_position.
        """
        str_list = list(preparred_input)
        str_list[current_head_position] = new_char
        preparred_input = ''.join(str_list)

        return preparred_input

    @staticmethod
    def _calculate_new_head_position(current_head_position: int, direction: str):
        """
        :current_head_position: The index of the string, the head of the tm is currently on
        
        :direction: The direction the head will be moving next
        """
        if str(direction).lower() == 'r':
            return current_head_position + 1

        if str(direction).lower() == 'l':
            return current_head_position - 1

        if str(direction).lower() == 'n':
            return current_head_position

    def run_machine(self, input: str):
        """
        :input: The word you want to give to the turingmachine, to calculate the results.

        Function that organizes the calculation-process of the input-string on the specified
        """
        if not self._check_input_match_alphabet(input):
            raise InputNotInAlphabet

        # We add 'B' to the input and also set starting position of the head to 4 because we added '...B' to the left of the input
        prepared_input = self._prepare_word_for_calculation(input)
        current_head_position = 4
        
        while self.current_state != self.ending_state:
            # First we print the configuration we are currently on
            printable = self._create_printable(prepared_input, self.current_state, current_head_position)
            print(printable)

            input_red = prepared_input[current_head_position]
            if input_red == '.':
                input_red = 'B'

            next_state, symbol_to_write, direction = self._calculate_step(self.current_state, input_red)

            # Now we apply all the three things to the current state, string and head-position
            prepared_input = self._replace_string(prepared_input, current_head_position, symbol_to_write)
            self.current_state = next_state
            current_head_position = self._calculate_new_head_position(current_head_position, direction)

        # Wir wollen den Endzustand noch zeigen
        printable = self._create_printable(prepared_input, self.current_state, current_head_position)
        print(printable)