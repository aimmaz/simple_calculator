#script uses no external libraries. 

#simple calculator for basic arithmetic operations. 

#This requests an input from user. 
request_operation = str(input("What arithmetic operation are we performing? The choices are {add, subtract, multiply, divide} \t"))

action = request_operation

if not request_operation in ["add","subtract","multiply","divide"]: 
    print("Incorrect selection, please specify available options!")
    
else:
    X = int(input("Please enter the  first integer of {} operation.\n".format(request_operation)))
    Y = int(input("Please enter the  second integer of {} operation.\n".format(request_operation)))

#This defines various operations 

#add operation
result = 0

if action == "add":
    result = X + Y

#subtract operation
elif action == "multiply": 
    result = X * Y

#multiply operation
elif action == "subtract":
    result = X - Y

#divide operation
elif action == "divide": 
    result = X / Y

print('The result is {}.'.format(result))
  
    
