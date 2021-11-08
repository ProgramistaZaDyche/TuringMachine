class TuringMachine:
    def __init__(self, title, state_names, alphabet, word_length, word, final_state, initial_state, states):
        self._title = title
        self._state_names = state_names
        self._alphabet = alphabet
        self._word_length = word_length
        self._word = word
        self._final_state = final_state
        self._initial_state = initial_state
        self.states = {}

        # list of lists with rules are being split into dictonaries of {string:list}
        for state in states:
            self.states[state[0]] = [case.split(",") for case in state[1:]]
