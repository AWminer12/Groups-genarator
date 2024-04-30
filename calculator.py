import random
from math import floor
import os
import csv


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


def better_zip(boys, girls):
    people = []
    if len(boys) > len(girls):
        longest = boys
        shortest = girls
    else:
        longest = girls
        shortest = boys
    for i,person in enumerate(longest):
        people.append(person)
        if i < len(shortest):
            people.append(shortest[i])
    return people


def Check_settings_main(result_gr, settings_list):
    Wrong = 0
    Positives = 0
    for group in result_gr:
        for person in group:
            for person_dict in settings_list:
                if person_dict['name'] == person[0]:
                    Wrong += CheckNegative(group, person, person_dict)
                    Positives += CheckPositive(group, person, person_dict)
    return Wrong, Positives


def read_settings_file(seti_file):
    settings_list = []
    plusses = 0
    with open(seti_file, 'r') as file:
        # open settings file and read it
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            settings_list.append(line)
            if line['withornot'] == '+':
                plusses +=1

    return settings_list, plusses


def CheckPositive(group, person, person_dict):
    Positives = 0
    if person_dict['withornot'] == '+':
        for checkperson in group:
            if person_dict['target-name'] == checkperson[0]:
                #print(f'HAPPY!! {person_dict['target-name']} zit bij {person[0]}')
                Positives += 1
    return Positives


def CheckNegative(group, person, person_dict):
    Negatives = 0
    if person_dict['withornot'] == '-':
        for checkperson in group:
            if person_dict['target-name'] == checkperson[0]:
                #print(f'NIET GOED!! {person_dict['target-name']} zit bij {person[0]}')
                Negatives += 1
    return Negatives


def read_people_file():
    people = []
    with open("namen.csv", "r") as file:
        #open the given file of names
        csv_reader = csv.reader(file)

        next(csv_reader)
        for line in csv_reader:
            people.append(line)
    people = [[x[0].lower().rstrip().lstrip(), x[1].lower().rstrip().lstrip()] for x in people]
    return people



def create_groups(group_nus, people):
    results = []
    prev_amount = 0
    for i,amount in enumerate(group_nus):
        results.append(people[prev_amount:prev_amount+amount])
        prev_amount +=amount
    save_groups(results)
    return results


def save_groups(results):
    with open("groupjes.csv", "w") as file:
        csv_writer = csv.writer(file)
        for group in results:
            csv_writer.writerow(group)


def main(printthinges=0):
    people = read_people_file()
    settings_list, max_oks = read_settings_file("genarator-settings.csv")
    i = 0
    Fixes =1  # init on 1 to enter whiile
    best_oks = 0
    for i in range(0, 10000):
        if i>0:
            random.shuffle(people)
        # mixing
        boys = [x for x in people if x[1] == 'jongen']
        girls = [x for x in people if x[1] == 'meisje']
        people = better_zip(boys, girls)
        group_format = calculate_groups(len(people), 5)
        calculated_groups = create_groups(group_format, people)
        Fixes, oks = Check_settings_main(calculated_groups, settings_list)
        i += 1
        if Fixes == 0 and oks > best_oks:
            best_result = calculated_groups
            best_oks = oks
            if printthinges == 1:
                print(f"fixes: {Fixes}, oks: {oks}")
                print(i)
                print(f"calced gr {calculated_groups}")
            if oks == max_oks:
                break
    return calculated_groups



if __name__ == '__main__':
    main(1)



