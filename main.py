from file_processing import DataFromFile
from os import listdir

if __name__ == '__main__':
    directory = "MTfiles\\"
    user_input = ""
    while user_input != "q":
        print("List of present MTfiles:")
        print([f for f in listdir(directory)])
        user_input = input("Please write the name of file of your liking or 'q' to quit.\n")
        print()
        if user_input == "q":
            exit()

        data_processor = DataFromFile(directory+user_input)
        machine = data_processor.create_turing_machine()
        machine.execute()
