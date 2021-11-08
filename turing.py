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
        self._states = states_dict
        # self._states = [State(key, case) for key, case in states_dict.items()]
        # self._actual_state = self._initial_state
        self._current_state = self._initial_state
        self._needle_position = 2
        self._needle = "".join([" "*(self._needle_position-1), "|\n", " "*(self._needle_position-1), "v"])

    def __execute(self):
        while self._current_state != self._final_state:
            # searching for rule line to execute
            to_execute = self.__find_rule()
            # changing current state of the machine
            self.__change_current_state(to_execute[1])
            # changing word according to the rule
            self.__change_character(to_execute[2])
            # moving the needle
            self.__move_needle(to_execute[3])
            # checking the position of the needle
            if self._needle_position == 1 or self._needle_position == self._word_length-1:
                self.__expand_word()

    def __expand_word(self):
        if self._needle_position == 1:
            self._word = "".join(["_", self._word])
        elif self._needle_position == self._word_length-1:
            self._word = "".join([self._word, "_"])
        self._word_length += 1
        self._needle_position += 1

    def __move_needle(self, move_command):
        if move_command == "r":
            self._needle_position += 1
        elif move_command == "l":
            self._needle_position -= 1
        self._needle = "".join([" "*(self._needle_position-1), "|\n", " "*(self._needle_position-1), "v"])

    def __change_character(self, character):
        self._word = "".join([self._word[:self._needle_position], character, self._word[self._needle_position + 1:]])

    def __find_rule(self):
        for rule in self._states[self._current_state]:
            if rule[0] == self._word[self._needle_position]:
                return rule

    def __change_current_state(self, new_state):
        self._current_state = new_state
        