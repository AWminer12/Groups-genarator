import random
from customtkinter import *
from math import floor

window = CTk()
window.geometry("500x400")

names_entry = CTkTextbox(border_color= "#da9100",border_width=  5,
                         master= window, scrollbar_button_color= "#ffd700", width= 150, scrollbar_button_hover_color= "#daa520")
names_entry.place(relx= 0.5, rely= 0.5, anchor= "center")
names_label = CTkLabel(text= "Enter names for group creation", font= ("times new roman", 15), text_color= "#da9100", master= window)
names_label.place(relx= 0.5, rely= 0.2, anchor= "center")
confirm_names = CTkButton(text= "Confirm", fg_color= "#32cd32", text_color="#ffffff", master= window)
confirm_names.place(relx= 0.5, rely= 0.9, anchor= "center")

#h

def calculate_groups(num_people, num_groups):
    num_people = int(num_people)
    num_groups = int(num_groups)
    group_size = floor(num_people/num_groups)
    remainder = num_people%num_groups
    result_groups = []
    for i in range(0, num_groups):
        g = group_size
        if remainder > 0:
            g += 1
            remainder -= 1
        result_groups.append(g)
    return result_groups


all_names = []

set_appearance_mode("dark")

window.mainloop()