import tkinter as tk


from Model import Model
from View import View
from tkinter import filedialog, INSERT


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self.model, self)

    def open_file(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_path:
            print(file_path)
            self.model.read_from_file(file_path)
            for name in self.model.students:
                self.view.text_box_students.insert(INSERT, name + '\n')




    def main(self):
        self.view.main()


