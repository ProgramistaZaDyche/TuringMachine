import unittest
import fileinput
import sys
from file_processing import DataFromFile


def create_machine(file_path, new_word):
    change_word(file_path, new_word)
    data_processor = DataFromFile(file_path)
    machine = data_processor.create_turing_machine()
    return machine.execute()  # returns tuple of (final_state, word_after_alternations)


def change_word(file_path, new_word):
    for line in fileinput.input(file_path):
        thekeyword = line.split(": ")[0]
        if thekeyword == "słowo" or thekeyword == "word":
            line = line.replace(line.split(": ")[1], new_word)
            sys.stdout.write(line)


class TestingCases(unittest.TestCase):
    def test_MT1_02(self):
        path = "MTfiles\\MT1_02.txt"
        word = "1111_111"
        new_word = create_machine(path, word)[1]
        self.assertEqual(new_word, "___1111111__", "The alternations made in the word are incorrect")


if __name__ == "__main__":
    unittest.main()
