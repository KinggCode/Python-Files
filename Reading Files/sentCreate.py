def main():
    infile_input = input("Please enter the infile: ")
    outfile_input = input("PLease enter the outfile: ")

    
    infile = open(infile_input,"r")
    outfile = open(outfile_input,"w")


    for i in infile.readlines():
        sentence = i.split()
        print(sentence)

main()
        
    
