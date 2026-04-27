with open('name.txt', 'r') as f:
    content = f.read()
    print(content)
    

with open("name.txt", "w") as f:
    f.write("This is Naymur before you\n")
    f.write("BSC in CSE\n")
    
with open("name.txt", "a") as f:
    f.write("Living in Mymensingh\n")
    f.write("I love to code\n")
    

line = ['\nI love python\n', 'I am new to python\n']    

with open("name.txt", "a") as f:
    f.writelines(line)

print(content)