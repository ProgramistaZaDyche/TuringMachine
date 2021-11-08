from file_processing import DataFromFile

if __name__ == '__main__':
    data_processor = DataFromFile("test1.txt")
    machine = data_processor.create_turing_machine()
    machine.execute()
