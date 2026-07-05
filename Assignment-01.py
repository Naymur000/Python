
# 1.student information

print("""
    +--------------------------+
        Enter your information
    +--------------------------+
     """)


Student_Name = input("Student Name: ")
Student_ID = int(input("Student ID: "))
Department = input("Department: ")


# 2.Subject Marks
print("""  
      
    +---------------+  
      Subject Marks
    +---------------+
      
      """)

dict_subjects = {}
list_subjects = ["Python", "Math", "English", "Physics", "ICT"]

for i in list_subjects:
    dict_subjects[i] = int(input(f"{i} : "))
    

# 3. Calculate Result

marks = list(dict_subjects.values())

print("""
      
      +------------------+
        Calculate Result
      +------------------+
      
      """)


total_marks = sum(marks)
Average_Marks = sum(marks)/len(marks)
Highest_Mark = max(marks)
Lowest_Mark = min(marks)


print("Total mark: ",total_marks)
print("Average mark: ",Average_Marks)
print("Highest mark: ",Highest_Mark)
print("Lowest mark: ",Lowest_Mark)



# 4. Grade Calculation

print("""
      
      +------------------+
        Grade Calculation
      +------------------+
      
      """)


Grade = ""

if Average_Marks >= 80 and Average_Marks <= 100:
    Grade = "A+"
elif Average_Marks >= 70 and Average_Marks < 80:
    Grade = "A"
elif Average_Marks >= 60 and Average_Marks < 70:
    Grade = "A-"
elif Average_Marks >= 50 and Average_Marks < 60:
    Grade = "B"
elif Average_Marks >= 40 and Average_Marks < 50:
    Grade = "C"
else:
    Grade = "F"

print("Grade : ", Grade)



# 5. Pass or Fail


print("""
      
      +------------------+
          Pass or Fail
      +------------------+
      
      """)


Status = ""

for i in marks:
    if i<40:
        Status = "Failed"
        break
    Status = "Passed"
    
print("Status: ",Status)
    
# 6. Password Verification

print("""
      
      +--------------------------+
          Password Verification
      +--------------------------+
      
      """)

while 1:
    password = input("Enter your password: ")
    
    if password == "python123":
        print("* Correct *")
        break
    print("Failed. Try again ")

# 7. String Operations


print("""
      
      +------------------------+
          String Operations
      +------------------------+
      
      """)


print("UpperCase: ",Student_Name.upper())
print("LowerCase: ",Student_Name.lower())
print("Length: ",len(Student_Name))
print("First three characters:", Student_Name[:3])
print("Last three characters:", Student_Name[-3:])


# 8. Set Example


print("""
      
      +------------------------+
            Set Example
      +------------------------+
      
      """)


sports = {"Football", "Cricket", "Badminton"}
clubs = {"Programming", "Cricket", "Photography"}

print("Common items:", sports.intersection(clubs))

print("All unique items:", sports.union(clubs))


# 9. Tuple Example

print("""
      
      +------------------------+
            Tuple Example
      +------------------------+
      
      """)


weekdays = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")

print("First day:", weekdays[0])

print("Last day:", weekdays[-1])

print("Total number of days:", len(weekdays))



# 10. Final Report


print("""
      
      +==============================+
              Student Report
      +==============================+
      
      """)

print("Name :", Student_Name)
print("ID :", Student_ID)
print("Department:", Department)

print("""
      
      """)

for k , v in dict_subjects.items():
    print(f"{k} : {v}")

print("""
      
      ----------------------
      
      """)

print("Total :", total_marks)
print("Average :", Average_Marks)
print("Highest :", Highest_Mark)
print("Lowest :", Lowest_Mark)

print("""
      
      """)

print("Grade :", Grade)
print("Status :", Status)

print("""
      
      ==============================
      
      """)