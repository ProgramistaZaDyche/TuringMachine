from states import State


class TuringMachine:
    def __init__(self, title, state_names, alphabet, word_length, word, final_state, initial_state, states_dict):
        self._title = title
        self._state_names = state_names
        self._alphabet = alphabet
        self._word_length = word_length
        self._word = word
        self._final_state = final_state
        self._initial_state = initial_state
        # self.states = states_dict
        self._states = [State(key, case) for key, case in states_dict.items()]

        self._actual_state = self._initial_state
