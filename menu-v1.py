#!/usr/bin/env python3

import sys
options = {"a":"Add item", "l":"List items", "q":"Log out"}

while True:
    opt = input("Option: ")
    try:
        print(f"You selected option {opt}: {options[opt]}")
        sys.exit(0)
    except KeyError:
        pass
