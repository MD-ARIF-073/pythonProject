# username = input("Your Name: ")
#
#
# # print(f"hello {username}!")
# print("Hello {}!".format(username))
#
#
#
#
# first_value = 32
# second_value = 4
#
#
# addition = first_value + second_value
# subtraction = first_value - second_value
# mul = first_value * 3
# div = first_value / 5
# div_int = first_value // 2
# remainder = first_value % 5
#
# print(f"div: {div_int}")
#
# print(f"rem: {remainder}")
#
# print(f"Addition: {addition}")
#
# print(f"Sub: {subtraction}")
#
# print(f"Mul: {mul}")
#
#
# person_name = "ishtiaq sani"
# food = "pizza"
# value1 = 73
#
# ishtiaq_with_value = person_name + " " + str(value1)
# print(ishtiaq_with_value)
#
# concatinated_string = person_name + food
#
# print(concatinated_string)
#
# print(f"length of name: {len(ishtiaq_with_value)}")


# grocery_list = ["rice", "tomato", "potato" ]
# print(grocery_list)
#
# grocery_list.sort()
# print(grocery_list)
#
#
# numbers = [1, 45, 76, 23, 39]
# sorted_list = sorted(numbers)
# # numbers.sort()
# print(numbers)
# print(sorted_list)

# l2 = list()
#
# second_item = grocery_list[1]
# print(grocery_list[-1])
# print(grocery_list[-2])
#
# print(second_item)
#
# print(grocery_list)
#
# grocery_list.append("water")
#
# print(grocery_list)
# print(l2)
# l2.append(78)
#
# print(l2)
#
# l2.append("computer")
#
# print(l2)

#
# marks = int(input("What is your marks in programming: "))
#
# def show_grade(grade):
#     print(f"You got: {grade}")
#
# if marks >= 80:
#     show_grade("A+")
# elif marks < 80 and marks >= 70:
#     show_grade("A")
# elif marks < 70 and marks >= 60:
#     show_grade("A-")
# elif marks > 33:
#     show_grade("Passed")
# else:
#     show_grade("Failed")
#
#
# print("Finished")
#
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# even_numbers = []
# starting = 0
# user_input = int(input("Limit: "))
# while starting <= user_input:
#     if is_even(starting):
#         even_numbers.append(starting)
#     #     print(f"{starting} is Even")
#     # else:
#     #     print(f"{starting} is Odd")
#     starting = starting + 1

# for num in range(0, user_input + 1):
#     if is_even(num):
#         even_numbers.append(num)
#
#
# print(f"Even numbers: {even_numbers}")
# print("Finished")


grocery = ["rice", "potato", "tomato", "water"]
#
# for item in grocery:
#     if item == "potato":
#         break
#     print(item)
#
# print("Finished")


# for i in range(0, 10, 3):
#     print(i)
#

for i in range(0, len(grocery)):
    print(grocery[i])                 # grocery list er index er value ta print hoitase