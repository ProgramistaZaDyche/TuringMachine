from file_processing import DataFromFile

if __name__ == '__main__':
    data_processor = DataFromFile("Other\\3_jezyk_bacb.txt")
    machine = data_processor.create_turing_machine()
    machine.execute()
