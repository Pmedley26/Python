#Integer, Arithmetic and Boolean Operators Exercise
#We are going to be working with 6 different variables

#create a variable and assign it the value of the addition of 2,3 and 4

#create a second variable and assign it the value of the multiplication of 4 and 5

#create a third variable and assign it the value of subtracting 3 from the result of dividing 10 by 2

#Once you have created these variables and their respective values

#create a fourth variable and assign it the value of adding the results of the first 3 variables (make sure this value is an integer)

#create a fifth variable that claims the value of the fourth variable is greater than the value of the second variable

#create a sixth variable that claims the value of the third variable is less than the value of the first variable

#At this point you should have six different values, four of which are integers and the remaining two Boolean. Finally I want you to print out the results of the following

#the value of the fourth variable

#first variable is less than the value of the second variable

#NOT the value of the fifth variable

#the value of both the fifth and sixth variables


Addition = 2 + 3 + 4
Multiplication = 5 * 4
Subtraction = 10/2 - 3


# When comparing data types, python will automatically convert the print function to equal "None" if the data types are not compatible.
#This is why we convert the result of the addition to an integer.
Result = int(Addition + Multiplication + Subtraction)
print(Result)

# create a fifth variable that claims the value of the fourth variable is greater than the value of the second variable
FifthVariable = Result > Multiplication







#If you did the test correctly, your output for the four print statements should be

31

True

False

True






