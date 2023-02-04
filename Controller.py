import tkinter.messagebox as mes
import random
from Model import Model
from View import View
from tkinter import filedialog, INSERT, messagebox
import sys
import os

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self.model, self)



    def open_students_file(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_path:
            sys.stdout = open(os.devnull, 'w')
            self.model.read_students_from_file(file_path)
            sys.stdout = sys.__stdout__
            for name in self.model.students:
                self.view.text_box_students.insert(INSERT, name + '\n')

    def open_tasks_file(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        if file_path:
            sys.stdout = open(os.devnull, 'w')
            self.model.read_tasks_from_file(file_path)
            sys.stdout = sys.__stdout__
            for name in self.model.tasks:
                self.view.text_box_tasks.insert(INSERT, name + '\n')

    def click_btn_mix(self):

        if len(self.model.students) > len(self.model.tasks):
            mes.showerror('Warning!!!', 'Ülesandeid on vähe või puuduvad!!')
        else:
            self.view.text_box_results.delete('1.0', 'end')
            self.model.shuffle_list()
            x = 0
            for name in self.model.students:
                self.view.text_box_results.insert(INSERT, name + ' - ' + self.model.tasks[x] + '\n')
                self.model.mix.append(name + " - " + self.model.tasks[x])
                x += 1

        if not self.model.students:

            messagebox.showwarning("Warning", "Failid puuduvad!!")

        elif not self.model.tasks:

           pass

    def click_btn_save(self):
        if not self.model.mix:
            messagebox.showwarning("Hoiatus", "Enne failide salvestamist valige failid.")
            return
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            for result in self.model.mix:
                file.write(result + "\n")
            file.close()

    def main(self):
        self.view.main()


