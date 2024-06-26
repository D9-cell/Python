#if we run the below code 
for line in open('script.py'):
    print(line,end='')
#the output will be -->
#import time
#print("Chai is here")
#username = "Deepon Das"
#print(username)


#if we run the below code which is alternative of for loop
f = open('script.py') 
while True:
    line = f.readline()
    if not line:break 
    print(line,end='')
#the output will be -->
#import time
#print("Chai is here")
#username = "Deepon Das"
#print(username)

#Another way is below 
f = open('script.py') 
f.readline()
#Under the hood readline() actually use __next__() and handles the exception.
#under te hood f will act as a iter(f)
#Below two is only applicable for file
iter(f) is f # --> True value returned
iter(f) is f.__iter__() # --> True value returned

#Another way is below 
f = open('script.py') 
f.__next__()
#but in this case at the end of the file this will give an error
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#StopIteration

I = iter(myList)
I # --> <list_iterator object at 0x000002914FA8A4A0>
# I is a list iterator which is pointing to the first memory reference of the myList and I will always store that.
#the __next__() will point to every item in the list but that doesn't effect what will store I
I.__next__() # --> 1
I.__next__() # --> 2
I.__next__() # --> 3
I.__next__() # --> 4

#range() and dictionary is also iterable

#I.__next__() and next(I) both are same

