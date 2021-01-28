print("Enter two numbers ")

first_num = int(input())
second_num = int(input())

print("Enter Operations ( +, -, *, /) ")
op = input()

def add(x, y):
    return x + y
def sub(x,y):
    return x - y

if op == "+":
  print("Result is ", add(first_num, second_num))

elif op == "-":
  print("Result is ", sub(first_num, second_num))



