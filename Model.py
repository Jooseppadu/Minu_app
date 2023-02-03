
class Model:
    def __init__(self):
        self.students = []


    def read_from_file(self, file_path):
        with open(file_path, "r", encoding='utf-8') as file:
            contents = file.readlines()
            for line in contents:
                line = line.strip()
                self.students.append(line)
            print(self.students)




