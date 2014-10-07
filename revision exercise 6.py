#Christopher pullen
#7-10-14
#statement revision exercise 6

print (" please enter a whole number when asked")

number_1 = int(input("please enter your first number"))
number_2 = int(input("please enter your second number"))
number_3 = int(input("please enter your third number"))


if number_1 >= number_2 and number_1 >= number_3: 
    print ("{0} is the largest!" .format (number_1))
elif number_2 >= number_1 and number_2 >= number_3:
           print (" {0} is the largest " .format (number_2))
elif number_3 >= number_1 and number_3 >= number_2:
                  print (" {0} is the largest " .format (number_3))
else:
    print("invalid number")
    
