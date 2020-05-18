import os

#Replace this variable with your directory. Use two backslashes.
champdirs = 'D:\\LoL\\Config\\Champions'
for root, dirs, files in os.walk(champdirs):

    for file_name in files:
        if "@blitz" in file_name:
            print("removing %s..." % root+'\\'+file_name)
            os.remove(root+'\\'+file_name)