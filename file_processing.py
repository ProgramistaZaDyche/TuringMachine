from turing import TuringMachine


class BadStateException(Exception):
    pass


class DataFromFile:
    """The underscore sign (_) is a default blank sign
    Steps in states are split with commas (,)
    There is no special sign indicating end of line
    List of lists with rules are being split into dictonaries of {string:list}"""

    def __init__(self, file_name):
        self.file_name = file_name

    def create_turing_machine(self):
        with open(self.file_name, "r") as file:
            content = file.readline()
            title = content.split(": ")[1]

            content = file.readline()
            state_names = content.split(": ")[1].split(",")

            content = file.readline()
            alphabet = content.split(": ")[1].split(",")

            content = file.readline()
            word_length = int(content.split(": ")[1])

            content = file.readline()
            word = [character for character in content.split(": ")[1]]
            word_length = self.__correct_word_length(word, word_length)

            content = file.readline()
            final_state = content.split(": ")[1]

            content = file.readline()
            initial_state = content.split(": ")[1]
            self.__correct_states(final_state, initial_state, state_names)

            states = []
            singular_state = []
            iterator = 0
            for line in file:
                singular_state.append(line.strip(" ,;:"))
                iterator += 1
                if iterator == len(alphabet):
                    iterator = 0
                    states.append(singular_state)
                    del singular_state
            states_dict = self.__states_to_dict(states)
            return TuringMachine(title, state_names, alphabet, word_length, word, final_state, initial_state, states_dict)

    @staticmethod
    def __correct_word_length(word, word_length):
        actual_length = len(word)
        if word_length != actual_length:
            print(f"Given word length is incorrect. Given word length is {word_length}"
                  f" while actual value is {actual_length}.")
            print("Worry not, the program shall continue it's work.")
        return actual_length

    @staticmethod
    def __correct_states(initial_state, final_state, state_names):
        if initial_state not in state_names:
            raise BadStateException("Given initial state is not in defined set of states, please correct the mistake.")
        if final_state not in state_names:
            raise BadStateException("Given final state is not in defined set of states, please correct the mistake.")
        if initial_state == final_state:
            raise BadStateException("Given initial state and final state are one and the same, "
                                    "please correct the mistake.")

    @staticmethod
    def __states_to_dict(states):
        states_dict = {}
        for state in states:
            states_dict[state[0]] = [case.split(",") for case in state[1:]]
        return states_dict
