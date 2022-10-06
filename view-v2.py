#!/usr/bin/env python3


def view(description, strings):
    print(description)
    for i in range(len(names)):
        print(f"    {i + 1}) {names[i]}")


names = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

view("Lista med namn", names)
print()
view("Lista med djur", animals)
