from turing import TuringMachine


class BadStateException(Exception):
    pass


class BadCharacterException(Exception):
    pass


class BadMovementInstructionException(Exception):
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
            title = content.split(": ")[1].strip(""" ,".""").upper()

            content = file.readline().strip("\n")
            state_names = [state.strip() for state in content.split(":")[1].lstrip().split(",")]

            content = file.readline().strip("\n")
            alphabet = [state.strip() for state in content.split(":")[1].lstrip().split(",")]

            content = file.readline().strip("\n")
            word_length = int(content.split(":")[1].lstrip())

            content = file.readline().strip("\n")
            word = "".join([character for character in content.split(":")[1].lstrip()])
            word = self.__surround_the_word(word)
            word_length = self.__correct_word_length(word)

            content = file.readline().strip("\n")
            final_states = [state.strip() for state in content.split(":")[1].lstrip().split(",")]
            # [state.strip() for state in content.split(":")[1].lstrip().split(",")]

            content = file.readline().strip("\n")
            initial_state = content.split(": ")[1].lstrip()
            self.__correct_states(initial_state, final_states, state_names)

            file.readline()  # keyword instruction
            states = []
            singular_state = []
            iterator = 0
            for line in file:
                iterator += 1
                singular_state.append(line.strip(" ,;:\n"))
                if iterator == len(alphabet)+1:
                    iterator = 0
                    temp = singular_state.copy()
                    states.append(temp)
                    singular_state.clear()

            states_dict = self.__states_to_dict(states)
            self.__check_the_dict(states_dict, state_names, alphabet)
            return TuringMachine(title, state_names, alphabet, word_length, word, final_states, initial_state,
                                 states_dict)

    @staticmethod
    def __correct_word_length(word):
        actual_length = len(word)
        return actual_length

    @staticmethod
    def __correct_states(initial_state, final_states, state_names):
        if initial_state not in state_names:
            raise BadStateException("Given initial state is not in defined set of states.")
        for state in final_states:
            if state not in state_names:
                raise BadStateException("There is an undefined set in the given set of final states.")
        if initial_state in final_states:
            raise BadStateException("Given initial state is in the set of final states.")

    @staticmethod
    def __states_to_dict(states):
        states_dict = {}
        for state in states:
            states_dict[state[0]] = [case.split(",") for case in state[1:]]
        return states_dict

    @staticmethod
    def __check_the_dict(states_dict, state_names, alphabet):
        for key, value in states_dict.items():
            if key not in state_names:
                raise BadStateException(f"There is a non-existent state in the instructions section:\n"
                                        f"{key}(Bad state): {value}\n"
                                        f"Existing states: {state_names}")
            for single_instruction in value:
                if single_instruction[1] not in state_names:
                    raise BadStateException(f"There is a non-existent state in the instructions section:\n"
                                            f"{key}: {value}\n"
                                            f"{single_instruction}\n"
                                            f"Existing states: {state_names}")
                if single_instruction[0] not in alphabet or single_instruction[2] not in alphabet:
                    raise BadCharacterException(f"There is a non-existent alphabet character in the "
                                                f"instructions section:\n"
                                                f"{key}: {value}\n"
                                                f"{single_instruction}"
                                                f"Existing chars: {alphabet}")
                if single_instruction[3] not in ["r", "l", "s"]:
                    raise BadMovementInstructionException(f"There is an unknown movement instruction in the "
                                                          f"instructions section:\n"
                                                          f"{key}: {value}\n"
                                                          f"{single_instruction}")

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
