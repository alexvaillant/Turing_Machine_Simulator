from typing import Dict

class FunctionDescrModel():
    """
    This class is used to save the information about a specific state and how it behaves when encountering a specific input_symbol 
    """
    def __init__(self, input_symbol: str, next_state: int, symbol_to_write: str, direction: str):
        self.input_symbol = input_symbol
        self.next_state = next_state
        self.symbol_to_write = symbol_to_write
        self.direction = direction


class StateFunctionModel():
    """
    This class saves all the Function-Descriptions of one single state.
    """
    def __init__(self, state_number: int, all_function_descr: Dict[str, FunctionDescrModel]):
        self.state_number = state_number
        self.all_function_descr = all_function_descr