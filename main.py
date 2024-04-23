import random
from customtkinter import *
from math import floor

window = CTk()
window.geometry("500x400")

frame1 = CTkFrame(master= window, fg_color= "#33FF68", border_color= "#07BE37", border_width= 2
                  , corner_radius= 25, width= 200, height= 75)
frame1.place(anchor= "nw", relx= 0.07, rely= 0.06)
entry1 = CTkEntry(master= frame1, placeholder_text= "Voer een naam in", corner_radius= 32)
entry1.place(anchor= "nw", rely= 0.2, relx= 0.1)

add_frame_button = CTkButton(master= window, hover_color= "#08BB37",
                             fg_color= "#01FF44", text= "Voeg kind toe")
add_frame_button.place(anchor = "nw", relx= 0.1, rely= 0.3)



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