with open('name.txt', 'r') as f:
    content = f.read()
    print(content)
    

with open("name.txt", "w") as f:
    f.write("This is Naymur before you\n")
    f.write("BSC in CSE\n")