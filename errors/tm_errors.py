
class InputNotInAlphabet(Exception):
    """
    This error is raised when the input_word has a symbol that is not in the input-alphabet.

    Arguments:
        message = explains what happened
    """
    def __init__(self, message="The input-word has symbols that aren't in the input-alphabet!"):
        self.message = message
        super().__init__(self.message)