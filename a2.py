try:
     num1 , num2 = eval(input("enter 2 numbers separated by comma, : "))
     print("the numbers are: ", num1,",", num2)
     operation = num1/num2
     print("the result is: ", operation)

except ZeroDivisionError:
     print("Do not enter 0 as a number")
except SyntaxError:
     print("the format is wrong please enter the numbers seperated by commas")
except:
     print("Wrong Input use integers")

else:
     print("there are no sort of exceptions GREAT! ")

finally:
     print("this line will print no matter what ")