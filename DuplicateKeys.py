
def searchFunct(source, query):
    #look to see if number the user typed is in the dictionary keys. If so, return the [list] of connected values. Otherwise, return an empty list.
    if query in source.keys():
        return source[query]
    else:
        return []



def main():
    fileDict = {}

    f = open("c:\\users\\david\\downloads\\file.tsv", 'r')
    for line in f:

        key, value = line.split("\t")
        value = value.strip("\n")
        #key = int(key)
        #value = int(value)
        #nice logic found on web to check if a key exists and append a value 
        if key in fileDict.keys():
            fileDict[key].append(value)

        else:
            #if key does not exists, create new key:value pair with the value being a list of a single value to start [value]
            #in the check above, we will append to the value list as new pairings are encountered in the data stream.
            fileDict[key] = [value]
    f.close()
    while True:
        searchKey = str(input("Please type in a number from 1 to 6474, type 'exit' to leave: "))
        if searchKey == "exit":
            break
        searchKey = int(searchKey)
        if searchKey in range(1, 6474 + 1):
            print(f'The number is connected to: {searchFunct(fileDict, str(searchKey))}')
            # pass
        else:
            print("Out of range, please try again")


if __name__ == "__main__":
    main()
