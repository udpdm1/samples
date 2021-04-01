'''
Source: IterateThroughObjects.py
Inefficient method to use recursion to iterate through a list, string and tuple.
'''
def printAll(seq):
    print(seq)
    if seq:
        #Print first iterable element of object at index 0 position.
        print(seq[0])
        #Recursion call passing the entire object *except* the first element.
        #Inefficient method especially if the object is large as a new object in the stack is created for each recursion.
        printAll(seq[1:])

mylist = ['Cat','Dog','Mouse']
mystring = 'CatDogMouse'
mytuple = (1,2,3,4,5)

printAll(mylist)
printAll(mystring)
printAll(mytuple)