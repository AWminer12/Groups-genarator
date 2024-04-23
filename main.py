import random
import tkinter as tk
import tempfile
from customtkinter import *
from math import floor
from PIL import *
import os

add_frame_x = 0.1
add_frame_y = -0.2

def create_child_frame():
    global i  # Ensure that i is a global variable

    i += 1

    # Create a new frame and entry widget
    frame = CTkFrame(master=scroll_frame, fg_color="#33FF68", border_color="#07BE37", border_width=2,
                     corner_radius=25, width=200, height=75)
    frame.place(anchor="nw", relx=0.07, rely=0.06 + i * 0.09)  # Adjust y-position based on i

    entry = CTkEntry(master=frame, placeholder_text="Voer een naam in", corner_radius=32)
    entry.place(anchor="nw", rely=0.2, relx=0.1)


    add_frame_button.place(relx= add_frame_x, rely= add_frame_y + i * 0.09)

    # Store references to the frame and entry widget in lists
    frames.append(frame)
    entries.append(entry)


# Initialize i and lists to store frame and entry references
i = 0
frames = []
entries = []




file_path = os.path.dirname(os.path.realpath(__file__))
plus_image =CTkImage(Image.open(file_path + "/plus_sign.png"))


window = CTk()
window.geometry("500x400")

scroll_frame = CTkScrollableFrame(master= window, bg_color= "transparent")
scroll_frame.place(anchor= "nw", relx= 0, rely = 0)



add_frame_button = CTkButton(master=scroll_frame, hover_color="#08BB37",
                             fg_color="#01FF44", text=" Voeg kind toe", image=plus_image, text_color= "#000000", command= create_child_frame)
add_frame_button.place(anchor = "nw", relx= add_frame_x, rely= add_frame_y)




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
