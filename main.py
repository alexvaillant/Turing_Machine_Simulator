from models.turingmachine import TuringMachineModel

import helper_modules.argument_parser as arg_parser

def main():
    # First get the items from the command line
    filename, input_word = arg_parser.get_command_line_args()
    tm = TuringMachineModel(filename)

    # run the machine with a given word
    tm.run_machine(input_word)

if __name__ == '__main__':
    main()