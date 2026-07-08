
sqr = lambda x: x**2
print(sqr(4))

sum = lambda x,y: x+y
print(sum(3,4))

data = [1, 20, 3, 4, 5]

sq_data = sorted(data)
print(sq_data)

age = {"naym": 25, "fakir": 30, "rakin": 23}
new_age = sorted(age.items(), key= lambda x:x[1])
print(new_age)