from time import sleep


class TuringMachine:
    def __init__(self, title, state_names, alphabet, word_length, word, final_states, initial_state, states_dict):
        self._title = title
        self._state_names = state_names
        self._alphabet = alphabet
        self._word_length = word_length
        self._word = word
        self._initial_word = word
        self._final_states = final_states
        self._initial_state = initial_state
        self._states = states_dict
        self._current_state = self._initial_state
        self._needle_position = 2
        self._needle = self.__create_needle()

    def execute(self):
        self.__introduce()
        while self._current_state not in self._final_states:
            print("===================")
            print(f"Current state: {self._current_state}")
            print(self._needle)
            print(self._word)

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

            sleep(1)
        print("===================")
        print("This is the last step.")
        print(f"Current state: {self._current_state}")
        print(self._needle)
        print(self._word)
        self.__create_raport()

    def __expand_word(self):
        if self._needle_position == 1:
            self._word = "".join(["_", self._word])
            self._needle_position += 1
        elif self._needle_position == self._word_length-1:
            self._word = "".join([self._word, "_"])
        self._word_length += 1

    def __move_needle(self, move_command):
        if move_command == "r":
            self._needle_position += 1
        elif move_command == "l":
            self._needle_position -= 1
        self._needle = self.__create_needle()

    def __set_needle(self):
        for i in range(len(self._word)):
            if self._word[i] != "_":
                self._needle_position = i
                self._needle = self.__create_needle()
                return

    def __create_needle(self):
        return "".join([" " * self._needle_position, "|\n", " " * self._needle_position, "V"])

    def __change_character(self, character):
        self._word = "".join([self._word[:self._needle_position], character, self._word[self._needle_position + 1:]])

    def __find_rule(self):
        for rule in self._states[self._current_state]:
            if rule[0] == self._word[self._needle_position]:
                return rule

    def __change_current_state(self, new_state):
        self._current_state = new_state

    def __introduce(self):
        print(f"Introduction of algorithm {self._title}\nWith given set of states: {self._state_names}\n"
              f"And alphabet: {self._alphabet}")

    def __create_raport(self):
        file = open(f"{self._title}_raport.txt", "w")
        file.write(f"Initial word: {self._initial_word}\n"
                   f"Instruction name: {self._title}\n"
                   f"Word after algorithm: {self._word}\n"
                   f"Ending state: {self._current_state}")
        file.close()
