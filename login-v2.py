#!/usr/bin/env python3

import sys

def login(users):
    while True:
        usr = input("User: ")
        passwd = input("Password: ")
        if usr in users and users[usr] == passwd:
            return usr
        else:
            print("Invalid username or password")

users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user1 = login(users1)
print(f"Welcome {user1}")

users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
user2 = login(users2)
print(f"Welcome {user2}")

