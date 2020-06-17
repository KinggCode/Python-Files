#Arthur: Eugene Parker

def FileSystem():
    inputFile = input("Please enter the input filename: ")
    destFile = input("Please enter the dest filename: ")

    infile = open(inputFile,"r")
    outfile = open(destFile,"w")
    view = infile.read()
    wlist = view.split()
    print(wlist)

    for message in wlist:
        print(message,end=" ", file=outfile)
    print("done!")


FileSystem()
