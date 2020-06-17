#Arthur : Eugene Parker


def monthCluster():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = eval(input("Enter the number of any month: "))

    pos = (n - 1)*3
    monthAbbrev = months[pos:pos+3]
    print(monthAbbrev)

monthCluster()
    
