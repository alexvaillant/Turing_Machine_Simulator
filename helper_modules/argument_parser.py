from typing import Tuple
import argparse

def _create_argument_parser():
    """
    We create the argument_parser with the args we need to run the TM.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('input_word')

    return parser


def get_command_line_args() -> Tuple[str]:
    """
    Get the specification made in the command line, in this case:
    1. Name of the TM-specification-file
    2. Word you want to run the TM with
    """
    parser = _create_argument_parser()
    args = parser.parse_args()

    return (args.filename, args.input_word)