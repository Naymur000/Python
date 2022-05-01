try: 
    with open("name.txt", "r") as f:
        content = f.read()
        print(content)
        
    print(10/0)
    x= int("123")
    a = [3,4,6]
    print(a[100])
    x= 10


except ZeroDivisionError:
    print("Error: Division by zero is not possible")


except FileNotFoundError:
    print("File not found")
    
except ValueError:
    print("String to integer is not possible")

except IndexError:
    print("Invalid Index")
    
except Exception as e:
    print("Some error occured!", e)
    
else:
    print("Code executed successfully")
    
finally:
    print("Finished !")
    
    