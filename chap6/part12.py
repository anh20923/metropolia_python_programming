def printlabels():
    global postnumber

    if postnumber == "00102":
        print("Parliament house: 00102")

    postnumber = "99999"

postnumber = "00102"

printlabels()

if postnumber == "99999":
    print("North Pole:", postnumber)