x = int(input("x = "))
operation = input("Operation(+,-,*,/): ")
y = int(input("y = "))

res = 0

if operation == "+":
    res = x + y
elif operation == "-":
    res = x -y
elif operation == "*":
    res = x * y
elif operation =="/":
    res= x/y

print("* "*20)
print('{} {} {} = {}'.format(x,operation,y,res))
print("* "*20)