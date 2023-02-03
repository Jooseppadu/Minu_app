import tkinter.messagebox as mes
import random
from Model import Model
from View import View
from tkinter import filedialog, INSERT


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self.model, self)

    def open_students_file(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_path:
            print(file_path)
            self.model.read_students_from_file(file_path)
            for name in self.model.students:
                self.view.text_box_students.insert(INSERT, name + '\n')

    def open_tasks_file(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_path:
            print(file_path)
            self.model.read_tasks_from_file(file_path)
            for name in self.model.tasks:
                self.view.text_box_tasks.insert(INSERT, name + '\n')

    def click_btn_mix(self):
        if len(self.model.students) > len(self.model.tasks):
            mes.showerror('Error', 'Ülesandeid on vähe')
        else:
            self.view.text_box_results.delete('1.0', 'end')
            self.model.shuffle_list()
            x = 0
            for name in self.model.students:
                self.view.text_box_results.insert(INSERT, name + ' - ' + self.model.tasks[x] + '\n')
                self.model.mix.append(name + " - " + self.model.tasks[x])
                x += 1

    def click_btn_save(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            for result in self.model.mix:
                file.write(result + "\n")
            file.close()

    def main(self):
        self.view.main()


