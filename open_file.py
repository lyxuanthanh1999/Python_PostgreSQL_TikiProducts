
try:
    with open("file.log") as file:
        read_data = file.read()
except:
    print("Couldn't open file.log")
    