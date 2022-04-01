import math


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')

print("this is a test")

# Printing count of each item in list
list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]

print("Original list ", list1)

count = dict()
for item in list1:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

print("Printing count of each item ", count)
print()

# get values from dictionary and add to list, without duplicates
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary's values: ", speed.values())
print("Dictionary's items: ", speed.items())

listNoDups = list()
for val in speed.values():
    if val not in listNoDups:
        listNoDups.append(val)

print("unique list ", listNoDups)
print()

# remove duplicates from a list, create a tuple, and find min and max number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
sample_list = list(set(sample_list))

print("unique list ", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))

# find list of students enrolled in both courses

math494 = {'rami': 40056879, 'felix': 458963210, 'tim': 40021589}
comp395 = {'rami': 40056879, 'anna': 45888087, 'tim': 40021589}

print(set(math494.keys()).intersection(set(comp395.keys())))
print(set(math494.keys()).intersection(comp395.keys()))  # set intersection
print()


# function that prints each name string
def string_name(*names):
    print(names)


# function that prints each name string
def integer_value(*numbers):
    return sum(numbers)


string_name("josie", "carol")
print(integer_value(1, 2, 3))
print()


# factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(8))


# addition and subtraction in a single return call
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction  # multiple return values


def calcul(a, b):
    return a + b, a - b


add, sub = calcul(40, 10)
print(add, sub)

res = calculation(40, 10)
print(res)
print()

# lambda expression to create a list from existing list

list3 = [2, 4, 8, 10, 12, 15]

multiples_of_4 = list(filter(lambda a: (a % 4 == 0), list3))
print(multiples_of_4)

# lambda, squares of numbers in a given list

squares_of_nums = map(lambda x: x * x, list3)
print(list(squares_of_nums))
print()

# lambda function vs list comprehension

list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lambda_list = list(map(lambda x: x * 2, list_))
print(lambda_list)

list_comp = [x * 2 for x in list_]
print(list_comp)

# input age

print("what is your age?")
age = int(input())

if age < 18:
    print("you are a minor")
elif 18 <= age < 65:
    print("you are legally an adult")
else:
    print("you are a senior")
