
numbers = [10, 20, 30, 40]

numbers.insert(0, 8)
numbers.append(45)
numbers.extend([50, 60])

different_types = ['hello', 10, 30, 20.3, [1, 2, 'yes'], {1, 4, 5, 5}, (1, 2)]

# for items in different_types:
#     print(items)

print(10 in different_types)

# print the last element in the list
print(different_types[-1])

# print the list in reverse
for items in reversed(different_types):
    print(items)

for number in reversed(numbers):
    number -= 2
print(numbers)  # no change in the list

for i in range(len(numbers)):
    numbers[i] -= 2
print(numbers)  # now values will change

######################################

myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(myList[:-2])  # omit last two elements in the list
myList[0:2] = ['x', 'y']  # update the first two elements in the list

myList.pop()  # delete the last element: returns the last element
del myList[3]  # delete the fourth element
del myList[2:4]  # delete elements starting from second element and also the 3rd element

myList.remove('x')  # delete a specified element from the list

print(myList)
print(myList[::2])  # print every second element


# concat two lists together
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# repeat elements a certain amount of time
print(list1 * 4)  # prints: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(len(list1))
print(max(list1))  # prints the maximum element in the list
print(min(list1))
print(sum(list1))

# string split into list
a = "hello-hi-namaste"
print(a.split('-'))

list1.sort()  # changes the original list
sorted(list1)  # does not change the original list





