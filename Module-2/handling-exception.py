try: 
    with open("name.txt", "r") as f:
        content = f.read()
        print(content)
        
    print(10/0)
    x= int("abc")
    a = [3,4,6]
    print(a[100])

except ZeroDivisionError:
    print("Error: Division by zero is not possible")


except FileNotFoundError:
    print("File not found")
    
except ValueError:
    print("String to integer is not possible")

except IndexError:
    print("Index error")