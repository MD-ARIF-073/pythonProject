from cgitb import reset


# def make_triple(x):
#     return x * 3
#
#
# my_marks = [10, 20, 30, 40]
# result = map(make_triple, my_marks)               # map takes a func and an iterable
# print(list(result))
#

# lambda

def my_function(func, arg):
    return func(arg)

print(my_function(lambda x: 2 * x, 5))


def my_function(func, arg):
    return func(arg)

print((lambda x, y: x + 5 * y)(2,3))


# filter

def is_even(x):
    return x % 2 == 0

my_numbers = [1,2,3,4,5,6,7,8,9]

result = filter(is_even, my_numbers)
print(list(result))


nums = [11,12,13,14]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)


# Generator is an iterable like list, tuple

def my_iterable():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in my_iterable():
    print(i)



def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
             yield i

even_nums_list = list(even_numbers(10))
print(even_nums_list)

# Decorator
# যদি কখনো এমন দরকার পরে যে একটা ফাংশনের ফাংশনালিটি একটু পরিবর্তন/পরিবর্ধন করা দরকার কিন্তু আমরা সেই ফাংশনের কোড পরিবর্তন করতে চাচ্ছি না। তখন ডেকোরেটর ব্যবহার করে আমরা সেই কাজটা করতে পারবো।

# def my_decorator(func):
#      def decorate():
#           print("--------------")
#          func()
#         print("--------------")
#      return decorate
#
#  def print_raw():
#      print("Clear Text")
#
# decorated_function = my_decorator(print_raw)
# decorated_function()
#
#
# print_raw = my_decorator(print_raw)
# print_raw()

# def my_decorator(func):
#     pass

#
# @my_decorator
# def print_text():
#     print("Hello World!")


# Recursion

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(7))


# def factorial(x):
#   return x * factorial(x-1)
#
# print(factorial(5))


def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)


print(is_odd(17))
print(is_even(23))

# Set

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)



# Has some duplicate eliments such as 1
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)

# To add an eliment to the set
nums.add(-7)

# To remove an element to the set
nums.remove(3)
print(nums)

# ইউনিয়ন = |
# ইন্টারসেকশন = &
# ডিফারেন্স = -
# সিমেট্রিক ডিফারেন্স = ^

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)


# #ইতোমধ্যে আমরা জেনেছি পাইথনে যে ডাটা স্ট্রাকচার গুলো আছে সেগুলো হচ্ছে - লিস্ট, ডিকশনারি, টাপল এবং সেট। কিন্তু একটা দ্বিধা দ্বন্দ্ব সব সময় কাজ করতে পারে - কোন সময় কোন ধরনের ডাটা স্ট্রাকচার ব্যবহার করা উচিৎ।
#
# নিচের অনুসিদ্ধান্ত গুলো কাজে আসতে পারে,
#
# ডিকশনারি -
#
# যখন key-value জোড় এর মাধ্যমে বেশ কিছু ভ্যালু নিয়ে কাজ করতে হবে
#
# যখন key এর উপর ভিত্তি করে ডাটা খুঁজে নেয়ার প্রয়োজন পর্বে বেশি
#
# যখন তখন ডাটা গুলোর পরিবর্তন দরকার পরলে
#
# লিস্ট -
#
# যখন ডাটা গুলোর র‍্যান্ডোম অ্যাক্সেস দরকার পরবে এবং তা আমরা খুব সহজে ইনডেক্স ধরে করতে পারি ।
#
# সাধারণ একটি iterable দরকার হলে লিস্ট নিয়ে কাজ করা যেতে পারে
#
# সেট -
#
# যখন এলিমেন্ট গুলোর মধ্যে ইউনিকনেস দরকার পরবে।
#
# যখন ডাটা গুলোর র‍্যান্ডোম অ্যাক্সেস দরকার পরবে না।
#
# টাপল -
#
# যখন ডাটা পরিবর্তনের দরকার একদমই পরবে না। টাপল immutable.


# itertools
# func like count, cycle, repeat

from itertools import count

for i in count(3):
    print(i)
    if i >= 11:
        break


from itertools import accumulate

my_numbers = [1, 2, 3, 4, 5, 6]
accumulated_numbers = accumulate(my_numbers)
list_of_accu_nums = list(accumulated_numbers)
print(list_of_accu_nums)



from itertools import takewhile

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_less_equal_six = takewhile(lambda x: x <= 6, my_numbers)
filtered_numbers = list(nums_less_equal_six)
print(filtered_numbers)



from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))