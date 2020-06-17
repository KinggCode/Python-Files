#Eugene Parker
#Assignment 3
#Source : Programming for Cs by John Zella


def fileViewer():
    filename = input("Enter the filename: ")
    outputFile = input("Enter the dest file: ")
    
    fileToken = open(filename,"r")
    destFile = open(outputFile,"w")
    view = fileToken.read()
    wlist = view.split()

    for words in wlist:
        print(words, file=destFile)

    fileToken.close()
    destFile.close()

    print("Data Packets sent from {} to {}".format(filename,outputFile))


fileViewer()
