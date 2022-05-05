# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
#!/usr/bin/python

list = ['abcd', 786, 2.23,'John', 70.2]
tinylist = [123, 'John']

print(list)		#Prints complete list
print(list[0])		#Prints first element of the list
print (list[1:3])	#Prints elements starting form 2nd till 3rd
print(list[2:])		#Prints elements starting from 3rd element
print(tinylist * 2)	#prints list two times
print(list + tinylist)	#prints concatenated lists

# printing all list items by using for loop
for x in range(len(list)):
	print(list[x])
#printing the list using * operator sparated space
print(*list)

# printing the list using * and separated by the comma
print(* list, sep=",")

#printing the list in new line
print(*list, sep="\n")

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'John')
print(tuple)		#Prints the complete tuple
print(tuple[0])		#Prints first element of the tuple
print(tuple[1:3])	#Prints elements of the tuple starting form 2nd till 3rd
print(tuple[2:])	#Prints elements of the tuple starting from 3rd element
print(tinytuple *2)	#Prints the contents of the tuple twice(* pachhi jati hunchha teti times print garchha)
print(tuple + tinytuple)#Prints concated/joins tuple

#printing tuples using for loop
print("Lenght of Tuple is:",  (len(tuple)))
for x in range(len(tuple)):
	print(tuple[x])

dict ={}
dict['One'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}

print(dict['One'])	         #Prints value for 'one' key
print(dict[2])		         #Prints value for '2' key
print(tinydict)		         #Prints complete dictionary
print(tinydict.keys())	     #Prints all the key
print(tinydict.values())     #Prints all the values
#iterate over key/value pair in dict and the print
for key, value in tinydict.items():
	print(key,":", value)


#convert form int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(x)

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))



# operator precendence
v = 4
w = 5
x = 8
y = 2
z = 0
z =(v+w) * x / y;
print ("Value of (v+w) * x/y is", z)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
