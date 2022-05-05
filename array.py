#array syntax
#arrayName = array.array(type code for data type,[array,items])
#how to create array
# class array.array(type code[,initialize]
#eg. import array as myarray            Creating alias(array as myarray)
#abc = myarray,array('d', [2.5, 4.9, 6.7])

import array
balance = array.array('i', [300,200,100,12,13,55,85,450])
print("Array last element is:",balance[-1])     #prints last index

print(balance[1]) # prints content in 1 no or prints 1st index
print(balance)  #prints whole content of balance
for i in balance:
    print(i, end=" ")   # prints variable i in the balance array
# accessing by :
# This operation is called a slicing operation
print(balance[:])
print(balance[1:4])     #4-1 index samma auuchha/ prints last -1 index

#insert
balance.insert(2, 150)
print(balance[:])

#modify
balance[0]=100
print(balance)

#array concatinations
#example
first = array.array('b', [1,2,3,4,5,6])
second = array.array('b', [7,8,9,10])
numbers = array.array('b')
numbers = first + second
print(numbers)
#printing concatenatied array
for i in numbers:
    print(i)

#removing items from an array
first.pop(2)      #REMOVES 3rd element and print the remaining
print(first)        #removes 2nd element and prints remaining
del first[1]
print(first)

#remove array items by value
numbers.remove(4)   #removes first 'number 4' 8 if 8 is written
print(numbers)
print("The length of the array is ", len(numbers))

#names = array.array('u', ["Purna Bahadur Karki", "Chandan Kumar Yadav", "Mukesh Shrestha", "Sabin Shreshtha", "Mina Marasini", "Nadim Priya Shrestha", "Nabin"])
#print(names[3])