x = int ( input("Enter a number: ") ) # ask the user to enter x

# check if the input is a valid number ( positive number )
if ( x > 0 ):    
    for i in range ( 1,x+1 ): 
        row = " "          # define an empty string variable for the current row
        for j in range ( 1, i+1 ): # loop to create the current row of numbers
            row += str ( j ) + ' '# add the number to the row followed by a space
            
        print ( row )
            
else:
    print ("Please enter a positive number!") # print an error message if the input is not a valid number 
