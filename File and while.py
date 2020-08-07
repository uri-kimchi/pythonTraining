firstName = ""
lastName = ""

while (firstName.upper() != "END"):
    firstName = input ("Enter First Name: ")
    lastName = input ("Enter Last Name: ")
    if (firstName == "David"):
        if (lastName=="Cohen"):
            print ("David the Cohen")
        elif (lastName == "Levi"):
            print ("This is the levi one")
        else:
            print ( "I have no clue which david is it")
    else:
        print (" OOOOOPSSSS")
print ("Enough is enough ")