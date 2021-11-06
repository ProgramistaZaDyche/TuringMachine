class BadStateException(Exception):
    pass


class DataFromFile:

    def __init__(self, file_name):
        with open(file_name, "r") as file:
            content = file.readline()
            self.title = content.split(": ")[1]

            content = file.readline()
            self.states = content.split(": ")[1].split(",")

            content = file.readline()
            self.alphabet = content.split(": ")[1].split(",")

            content = file.readline()
            self.word_length = int(content.split(": ")[1])

            content = file.readline()
            self.word = [character for character in content.split(": ")[1]]
            self.__correct_word_length()

            content = file.readline()
            self.final_state = content.split(": ")[1]

            content = file.readline()
            self.initial_state = content.split(": ")[1]

    def __correct_word_length(self):
        actual_length = len(self.word)
        if self.word_length != actual_length:
            print(f"Given word length is incorrect. Given word length is {self.word_length}"
                  f" while actual value is {actual_length}.")
            self.word_length = actual_length
            print("Worry not, the programme shall continue it's work.")

    def __correct_state(self):
        if self.initial_state not in self.states:
            raise BadStateException("Given initial state is not in defined set of states, please correct the mistake.")
        if self.final_state not in self.states:
            raise BadStateException("Given final state is not in defined set of states, please correct the mistake.")
        if self.initial_state == self.final_state:
            raise BadStateException("Given initial state and final state are one and the same, "
                                    "please correct the mistake.")
