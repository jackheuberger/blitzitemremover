import os

#Replace PATH_GOES_HERE with the path to your champions directory. Use two backslashes.
#This is located under league_install/config/Champions

champdirs = 'PATH_GOES_HERE'
for root, dirs, files in os.walk(champdirs):

    for file_name in files:
        if "@blitz" in file_name:
            print("removing %s..." % root+'\\'+file_name)
            os.remove(root+'\\'+file_name)
