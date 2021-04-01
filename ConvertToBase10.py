'''
Sample method to covert any number through Base16 to Base10
'''

#Map alphanumeric representations of unique number symbols in the numbering systems through Base16 with their
# associated quantity value for lookup using a dictionary object for storage.
#  
mydict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
def repToDecimal(mystring,mybase):
    numbase10 = 0
    digitcount = 0
    for digit in mystring[::-1]:
        #
        #The following equation is what is used to take a number in a particular base and translate it to Base10
        #Example: 123 Base8 equals:
        #1 times 13^2 + 2 times 13^1 + 3 times 13^0 = 198
        #
        numbase10 += mydict[digit] * mybase ** digitcount #digitcount represents our linear position in the string used as exponent of original Base
        digitcount += 1

    return numbase10

def main():
    #Test run of 123 Base 13
    print(f'123 in Base13 is equal to: {repToDecimal("123",13)} in Base10')


if __name__ == "__main__":
    main()

