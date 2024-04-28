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


def read_csv():
    people = []
    with open("namen.csv", "r") as file:
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
        results.append([i+1, people[prev_amount:prev_amount+amount]])
        prev_amount +=amount
    save_groups(results)
    return results


def save_groups(results):
    with open("groupjes.csv", "w") as file:
        csv_writer = csv.writer(file)
        for group in results:
            csv_writer.writerow(group)


def main():
    people = read_csv()
    print(people)
    boys = [x for x in people if x[1] == 'jongen']
    girls = [x for x in people if x[1] == 'meisje']
    people = better_zip(boys, girls)
    group_format = calculate_groups(len(people), 5)
    print(create_groups(group_format, people))


if __name__ == '__main__':
    main()








