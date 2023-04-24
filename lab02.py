import glob


def main():
    list1 = []
    for x in range(1, 21):
        list1.append(x)
    print(list1)

    list1Squares = []
    for x in list1:
        list1Squares.append(x**2)
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
    listOfFiles = [file1,file2,file3,file4]
    for x in listOfFiles:
        minor = listOfFiles.index(x)
        for i in range(listOfFiles.index(x)+1,len(listOfFiles)):
            if listOfFiles[minor].creationDate > listOfFiles[i].creationDate:
                minor = i
        aux = listOfFiles[minor]
        listOfFiles[minor] = x
        x = aux

    for x in listOfFiles:
        print("-> ",x.creationDate)


    listFiles = glob.glob('/Users/martin/Downloads/*')
    print(listFiles)

if __name__ == "__main__":
    main()

