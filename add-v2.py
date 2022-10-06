#!/usr/bin/env python3

def add(prompt, strings):
    new_s = input(prompt)
    strings.append(new_s)
    return strings

ducks = ["Huey", "Dewey", "Louie"]

print(f"Ducks: {ducks}")

add("Add a duck: ", ducks)

print(f"Ducks: {ducks}")

composers = ["Mozart", "Bach"]
print(f"Composers: {composers}")
print()

add("Add a composer: ", composers)

print(f" Composers: {composers}")
print()
