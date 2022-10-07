#!/usr/bin/env python3

import sys

def view(description, strings):
    print(description)
    for k, v in strings.items():
        print(f"    {k}) {v}")


def menu(title, prompt, options):
    view(title, options)
    while True:
        opt = input(prompt)
        if opt in options:
            return opt


def login(users):
    while True:
        usr = input("User: ")
        passwd = input("Password: ")
        if usr in users and users[usr] == passwd:
            return usr
        else:
            print("Invalid username or password")
            opt = menu("Try again?", "Option: ", {"q": "Quit", "r": "Try again"})
            if opt == "q":
                return None

users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

user = login(users)
print(user)
