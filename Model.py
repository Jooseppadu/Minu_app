import random


class Model:
    def __init__(self):
        self.mix = []
        self.students = []
        self.tasks = []


    def read_students_from_file(self, file_path):
        with open(file_path, "r", encoding='utf-8') as file:
            contents = file.readlines()
            for line in contents:
                line = line.strip()
                self.students.append(line)
            print(self.students)

    def read_tasks_from_file(self, file_path):
        with open(file_path, "r", encoding='utf-8') as file:
            contents = file.readlines()
            for line in contents:
                line = line.strip()
                self.tasks.append(line)
            print(self.tasks)

    def shuffle_list(self):
        random.shuffle(self.tasks)




