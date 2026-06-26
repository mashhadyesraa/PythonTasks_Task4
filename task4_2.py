def calculator(a,b,operation):
    result=0.0
    if operation=="add":
        result=a+b
    elif operation=="subtract":
        result=a-b
    elif operation=="multiply":
        result=a*b
    elif operation=="divide":
        result=a/b
    return result

a=float(input("Enter the First No!"))
b=float(input("Enter the Second No!"))
op=input("Ener your desired Operation (add, subtract, multiply,divide)")
if op == "add" or op == "subtract" or op == "multiply" or op == "divide":
    if op!="divide" and b!=0:
        print(f"the result of {op} with {a} and {b} is : {calculator(a,b,op):.2f}")
    else:
        print("Error! Can't divide by zero")

else:
        print("This operation isn't available right now!")






