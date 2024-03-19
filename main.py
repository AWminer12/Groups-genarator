import random
from customtkinter import *
from math import floor

window = CTk()
window.geometry("450x500")



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
for i in range(1, 27):
    child = [1, f"Joe{i}", 0, 0, 1]
    all_names.append(child)
print(all_names)
print(len(all_names))

print(calculate_groups(len(all_names), input("how many groups do you want?\n")))

set_appearance_mode("light")

window.mainloop()