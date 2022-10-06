#!/usr/bin/env python3

import sys

users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
while True:
    usr = input("User: ")
    passwd = input("Password: ")
    if usr in users and users[usr] == passwd:
        print(f"Welcome {usr}")
        sys.exit(0)
    else:
        print("Invalid username or password")
