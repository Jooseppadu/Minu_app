from logging import root
from tkinter import *
from tkinter import scrolledtext

class View(Tk):
    def __init__(self, model, controller):
        super().__init__()  # Super on selleks,et kasutada tkinterit
        self.model = model
        self.controller = controller
        self.title("Ülesanded")
        self.geometry("900x500")
        self.frame_top, self.frame_bottom = self.create_two_frames()
        self.create_all_buttons()
        self.text_box_students, self.text_box_tasks, self.text_box_results = self.text_box()

    def main(self):
        self.mainloop()




    def create_two_frames(self):       # Teeme kaks frame
        frame_top = Frame(self, bg='#0096FF', height=50)  # sinine
        frame_bottom = Frame(self, bg='#EBEB00') # kollane

        frame_top.grid(row=0, column=0)
        frame_bottom.grid(row=0, column=1)

        return frame_top, frame_bottom


    def create_all_buttons(self):
        self.btn_students = Button(self.frame_top, text="Students", command=self.controller.open_students_file)
        self.btn_students.grid(row=0, column=0, padx=5, pady=2, sticky=EW)

        self.btn_tasks = Button(self.frame_top, text="Tasks", command=self.controller.open_tasks_file)
        self.btn_tasks.grid(row=1, column=0, padx=5, pady=2, sticky=EW)


        self.btn_mix = Button(self.frame_top, text="Mix", command=self.controller.click_btn_mix)
        self.btn_mix.grid(row=0, column=2, padx=5, pady=2, sticky=EW)


        self.btn_save = Button(self.frame_top, text="Save", command=self.controller.click_btn_save)
        self.btn_save.grid(row=1, column=2, padx=5, pady=2, sticky=EW)

        return self.btn_students, self.btn_tasks, self.btn_mix, self.btn_save


    def text_box(self):


        # Loon tekstiväljad.
        Label(self.frame_bottom, text='Students').grid(row=1, column=0)
        text_area_students = scrolledtext.ScrolledText(self.frame_bottom, wrap=WORD, width=20, height=20,
                                                       font=("Times New Roman", 15))
        text_area_students.grid(row=0, column=0, pady=10, padx=10)


        Label(self.frame_bottom, text='Tasks').grid(row=1, column=2)
        text_area_tasks = scrolledtext.ScrolledText(self.frame_bottom, wrap=WORD, width=20, height=20,
                                                    font=("Times New Roman", 15))
        text_area_tasks.grid(row=0, column=2, pady=10, padx=10)

        Label(self.frame_bottom, text='Results').grid(row=1, column=3)
        text_area_results = scrolledtext.ScrolledText(self.frame_bottom, wrap=WORD, width=20, height=20,
                                                    font=("Times New Roman", 15))
        text_area_results.grid(row=0, column=3, pady=10, padx=10)

        return text_area_students, text_area_tasks,  text_area_results