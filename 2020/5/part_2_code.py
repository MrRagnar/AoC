#!/usr/bin/python
import sys
f = open("input", "r")
input = f.read().splitlines()

def split_list(rows):
    part = len(rows)//2
    return rows[:part], rows[part:]

def calculate_row(sequence):
    r = list(range(128))
    for step in list(sequence):
        if step == "F":
            f, b = split_list(r)
            r = f
        if step == "B":
            f, b = split_list(r)
            r = b
    return(int(r[0]))

def calculate_seat(sequence):
    s = list(range(8))
    for step in list(sequence):
        if step == "L":
            l, f = split_list(s)
            s = l
        if step == "R":
            l, r = split_list(s)
            s = r
    return(int(s[0]))

seat_id = []
for sequence in input:
    row = calculate_row(sequence[:7])
    seat = calculate_seat(sequence[7:10])
    seat_id.append(row * 8 + seat)

low_id = min(seat_id)
high_id = max(seat_id)
seat_id_range = range(low_id, high_id)
seat = sorted(set(seat_id_range).difference(seat_id))
print(seat[0])
