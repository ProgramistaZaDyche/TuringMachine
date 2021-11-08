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
            content = file.readline().strip("\n")
            title = content.split(": ")[1]

            content = file.readline().strip("\n")
            state_names = content.split(":")[1].lstrip().split(",")

            content = file.readline().strip("\n")
            alphabet = content.split(":")[1].lstrip().split(",")

            content = file.readline().strip("\n")
            word_length = int(content.split(":")[1].lstrip())

            content = file.readline().strip("\n")
            word = "".join([character for character in content.split(":")[1].lstrip()])
            word = self.__surround_the_word(word)
            word_length = self.__correct_word_length(word, word_length)

            content = file.readline().strip("\n")
            final_state = content.split(":")[1].lstrip()

            content = file.readline().strip("\n")
            initial_state = content.split(": ")[1].lstrip()
            self.__correct_states(initial_state, final_state, state_names)

            file.readline()
            states = []
            singular_state = []
            iterator = 0
            for line in file:
                singular_state.append(line.strip(" ,;:\n"))
                if iterator == len(alphabet):
                    iterator = 0
                    temp = singular_state.copy()
                    states.append(temp)
                    singular_state.clear()
                iterator += 1

            states_dict = self.__states_to_dict(states)
            return TuringMachine(title, state_names, alphabet, word_length, word, final_state, initial_state, states_dict)

    @staticmethod
    def __correct_word_length(word, word_length):
        actual_length = len(word)
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

    @staticmethod
    def __surround_the_word(word):
        if word[0] == "_":
            if word[1] == "_":
                pass
            else:
                word = "_" + word
        else:
            word = "__" + word

        if word[-1] == "_":
            if word[-2] == "_":
                pass
            else:
                word = word + "_"
        else:
            word = word + "__"
        return word
