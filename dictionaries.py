#!/usr/bin/env python3

users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}

print("Användare\n")
for user in users:
    print(f"    {user}")
print("\n")

print("Användare och lösenord\n")
for user, password in users.items():
    print(f"    {user}) {password}")
print("\n")

data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

print("Användare och deras data\n")
for user, userdata in data.items():
    print(f"    {user}) {userdata}")
print("\n")

user = input("Slå upp användare: ")
try:
    print(f"Data lagrat för {user}: {data[user]}")
except KeyError:
    print(f"Användaren {user} finns inte")
