import os

# Replace PATH_GOES_HERE with the path to your champions directory. Use two backslashes.
# This is located under league_install/config/Champions

print("Paste the path to your Champions folder.")
print("EX: C:\Riot Games\League of Legends\Config\Champions")
path = input()
champdir = ""

for char in path:
    if (char == "\\"):
        champdir += "\\"
    champdir += char

for root, dirs, files in os.walk(champdir):
    for file_name in files:
        if "@blitz" in file_name:
            print("removing %s..." % root+'\\'+file_name)
            os.remove(root+'\\'+file_name)
