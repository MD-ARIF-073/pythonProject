

fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# Lets make juice with these fruits

start_index = 0
max_index = len(fruits) - 1

while start_index <= max_index: # Work until this condition is True
    fruit = fruits[start_index]
    print(fruit + " Juice!")

    start_index = start_index + 1


fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# Lets make juice with these fruits

for fruit in fruits:
    print(fruit + " Juice!")



# start with 10
# end with 0
# step size -2
for i in range(10, 0, -2):
     print(i)