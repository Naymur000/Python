# 1. Add Expense

def add_expense(file):
      try:
            with open(file , "r") as f:
                  lines = f.readlines()
            
            Expense_ID = input("Enter Expense_ID: ")
            Date = input("Enter date: ")
            Category = input("Enter category: ")
            Description = input("Enter Description: ")
            while 1:
                  Amount = float(input("Enter amount: "))
                  if Amount < 0:
                        print("Amount cannot be negative.")
                  else:
                        break
            
            data = []
            data.append(Expense_ID)
            data.append(Date)
            data.append(Category)
            data.append(Description)
            data.append(str(Amount))

            with open(file, "a") as f:
                  f.write(",".join(data) + "\n")
      
      except FileNotFoundError:
            print("No expense records found")
      except ValueError:
            print("Invalid amount! Please enter a valid number")
      


# 2. View All Expenses

def view_expenses(file):
      try:
            with open(file, "r") as f:
                  lines = f.readlines()
            if not lines:
                  raise Exception("No expenses available!")
            else:
                  for line in lines:
                        line = line.strip().split(",")
                        print(f"""
                              
                              Expense ID : {line[0]}
                              Date : {line[1]}
                              Category : {line[2]}
                              Description: {line[3]}
                              Amount : {line[4]}
                        ------------------------------
                                    """)
      except FileNotFoundError:
            print("No expense records found")
      except Exception as e:
            print(e)



# 3. Search Expense

def search_expense(id, file):
      try:
            found = False
            with open(file, "r") as f:
                  lines = f.readlines()
                  if not lines:
                        raise Exception("No expenses available!")
                  else:
                        for line in lines:
                              line = line.strip().split(",")
                              if int(line[0]) == id:
                                    found = True
                                    print("Expense Found\n")
                                    print(f"""
                                          
                              Expense ID : {line[0]}
                              Date : {line[1]}
                              Category : {line[2]}
                              Description: {line[3]}
                              Amount : {line[4]}
                        --------------------------------
                                          
                                          """)
                                    break
                        if found == False:
                              print("Expense not found\n")
                  
      except FileNotFoundError:
            print("No expense records found")
      except Exception as e:
            print(e)



# 4. Update Expense

def update_expense(id, file):
      try:
            with open(file, "r") as f:
                  lines = f.readlines()
                  if not lines:
                        raise Exception("No expenses available!")
                  else:               
                        index = 0
                        for line in lines:
                              line = line.strip().split(",")
                              if int(line[0]) == id:
                                    line[1] = input("Update date: ")
                                    line[2] = input("Update Category: ")
                                    line[3] = input("Update description: ")
                                    while 1:
                                          line[4] = float(input("Update amount: "))
                                          if line[4] < 0:
                                                print("Amount cannot be negative.")
                                          else:
                                                line[4] = str(line[4])
                                                break                      
                                    
                                    lines[index] = ",".join(line) + "\n"
                                    break
                              index += 1
                              
                        with open("expenses.txt", "w") as f:
                              f.writelines(lines)
                  
      except FileNotFoundError:
            print("No expense records found")
      except ValueError:
            print("Invalid amount! Please enter a valid number")
      except Exception as e:
            print(e)
            

            
# 5. Delete Expense

def delete_expense(id, file):
      try:
            with open(file , "r") as f:
                  lines = f.readlines()
                  if not lines:
                        raise Exception("No expenses available!")
                  else:             
                        with open(file, "w") as f:
                              for line in lines:
                                    line = line.strip().split(",")
                                    if id == int(line[0]):
                                          continue
                                    f.write(",".join(line) + "\n")
      except FileNotFoundError:
            print("No expense records found") 
      except Exception as e:
            print(e)



# 6. Expense Summary

def expense_summary():
      
      with open("expenses.txt" , "r") as f:
            lines = f.readlines()
      
      total_expense = 0
      expense_list = []
      for line in lines:
            line = line.strip().split(",")
            total_expense += float(line[4]) 
            expense_list.append(float(line[4]))
            
      if len(lines) == 0 :
            average = "None"
            mx = "None"
            mn = "None"          
      else:
            average = float(total_expense/len(lines))
            mx = max(expense_list)
            mn = min(expense_list)
      
      
      print(f"""
            ========= Expense Summary =========
            
                  Total Expenses : {len(lines)}
                  Total Spending : {total_expense} BDT
                  Average Expense : {average} BDT
                  Highest Expense : {mx} BDT
                  Lowest Expense : {mn} BDT
                  
            ------------------------------------
            """)
                  
            
            
def main():
    while 1:
        print("\n========= Expense Tracker =========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Expense Summary")
        print("7. Exit")

        try:
            choice = int(input("Choose: "))

            if choice == 1:
                file = input("Enter file name: ")
                add_expense(file)

            elif choice == 2:
                file = input("Enter file name: ")
                view_expenses(file)

            elif choice == 3:
                expense_id = int(input("Enter expense id: "))
                file = input("Enter file name: ")
                search_expense(expense_id, file)

            elif choice == 4:
                expense_id = int(input("Enter expense id: "))
                file = input("Enter file name: ")
                update_expense(expense_id, file)

            elif choice == 5:
                expense_id = int(input("Enter expense id: "))
                file = input("Enter file name: ")
                delete_expense(expense_id,file)

            elif choice == 6:
                expense_summary()

            elif choice == 7:
                print("Program exited successfully.")
                break

            else:
                print("Invalid choice! Please select a valid option.")

        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 7.")


main()