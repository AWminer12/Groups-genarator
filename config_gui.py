from customtkinter import *
from tkinter import IntVar
import csv
import calculator
from CTkMessagebox import *
import sys


def save_settings():
    with open('genarator-settings.csv', 'w') as file:
        for i in range(0, len(boxes['person'])):
            p = boxes['person'][i].get()
            if p == '-':
                continue
            c = boxes['choice'][i].get()
            if c == '-':
                continue
            elif c == 'met':
                c = '+'
            else:
                c = "-"

            p2 = boxes['person2'][i].get()
            if p2 == '-':
                continue
            file.write(f"{p}, {c}, {p2}\n")
            calculator.main(amount_gr=p_p_gr_var.get())
            window.destroy()
            sys.exit()


def main():
    global window, boxes, p_p_gr_var

    def update_label(*args):
        edit_label.configure(text=f"aantal groepen:\n{p_p_gr_var.get()}")

    window = CTk()
    window.geometry("600x400")

    with open("namen.csv", "r") as file:

        boxes = {
            'person': [],
            'choice': [],
            'person2': []
        }

        p_p_gr_var = IntVar()
        p_p_gr_var.set(5)
        p_p_gr_var.trace_add("write", update_label)  # Add the trace to update the label

        reader = csv.reader(file)
        people = {}
        frame = CTkScrollableFrame(master=window, height=1000, width=1000, bg_color="transparent")
        edit_p_per_gr = CTkSlider(master=frame, from_=1, to=10, number_of_steps=9, hover=True, variable=p_p_gr_var)
        edit_label = CTkLabel(master=frame, text=f"aantal groepen:\n{p_p_gr_var.get()}")
        edit_p_per_gr.grid(column=2, row=1, padx=15, pady=10)
        edit_label.grid(column=2, row=0, padx=15, pady=10)
        y = 15
        for line in reader:
            key, value = line
            people[key] = value
        persons = people.keys()
        persons = list(persons)
        persons.insert(0, "-")
        for i in range(2, int(len(persons) * 1.5 + 2)):
            person_box = CTkComboBox(master=frame, values=persons)
            person_box2 = CTkComboBox(master=frame, values=persons)
            choice_box = CTkComboBox(master=frame, values=["-", "met", "zonder"])
            person_box.grid(row=i, column=1, padx=15, pady=10)
            choice_box.grid(row=i, column=2, padx=10, pady=10)
            person_box2.grid(row=i, column=3, padx=15, pady=10)
            boxes['person'].append(person_box)
            boxes['choice'].append(choice_box)
            boxes['person2'].append(person_box2)

        done = CTkButton(text="Generate", command=save_settings, master=frame)
        done.grid(row=int(len(persons) * 1.5) + 3, column=2, pady=50)

        frame.pack()

    set_appearance_mode("dark")  # Modes: "system" (default), "light", "dark"
    set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"
    window.mainloop()


if __name__ == '__main__':
    main()
