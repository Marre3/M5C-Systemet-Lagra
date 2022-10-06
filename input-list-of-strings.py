#!/usr/bin/env python3

def add(prompt, strings):
    new_s = input(prompt)
    strings.append(new_s)
    return strings

def view(description, strings):
    print(description)
    for i in range(len(strings)):
        print(f"    {i + 1}) {strings[i]}")

strings = []
n = 3

print(n)
for _ in range(n):
    add("Input string: ", strings)

view(f"Du har matat in följande {n} strängar", strings)
