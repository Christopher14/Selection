#Christopher pullen
#3-10-14
#statement revision exercise 4

print (" please enter a whole number when asked")

number_1 = int(input("please enter your first number"))
number_2 = int(input("please enter your second number"))

if number_1 > number_2:
    print ("{0} is larger!" .format (number_1))
elif number_2 > number_1:
           print (" {0} is larger " .format (number_2))
else:
                  print ("your numbers are equal")
