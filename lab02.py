import glob


def identicalFiles(file1, file2):
    if file1 == file2:
        return True
    else:
        return False


def lookForDuplicates(list):
    listAux = []     #auxiliar list to save just the name of each file
    for x in list:
        listAux.append(x[x.rfind("/"):])
    print(listAux)
    aux = False
    for y in listAux:    #look for duplicates in the list with the files' names
        for i in range(listAux.index(y) + 1, len(listAux)):
            if identicalFiles(y, listAux[i]):
                print("The files in the positions ", listAux.index(y), " and ", i, "are duplicated")
                aux = True
    if not aux:
        print("There are no duplicated files.")


def main():
    list1 = []
    for x in range(1, 21):
        list1.append(x)
    print(list1)

    list1Squares = []
    for x in list1:
        list1Squares.append(x ** 2)
    print(list1Squares)

    list1EvenValues = []
    for x in list1:
        if x % 2 == 0:
            list1EvenValues.append(x)
    print(list1EvenValues)

    class Files:
        def __init__(self, name, creationDate):
            self.name = name
            self.creationDate = creationDate

    file1 = Files("file1", 20200123)
    file2 = Files("file2", 20220413)
    file3 = Files("file3", 20181003)
    file4 = Files("file4", 20210918)
    listOfFiles = [file1, file2, file3, file4]
    for x in listOfFiles:
        minor = listOfFiles.index(x)
        for i in range(listOfFiles.index(x) + 1, len(listOfFiles)):
            if listOfFiles[minor].creationDate > listOfFiles[i].creationDate:
                minor = i
        aux = listOfFiles[minor]
        listOfFiles[minor] = x
        x = aux

    for x in listOfFiles:
        print("-> ", x.creationDate)

    listFiles = glob.glob('/Users/martin/Documents/Uni/3.Semester/Info3/lab02/test/**/*')
    lookForDuplicates(listFiles)


if __name__ == "__main__":
    main()
