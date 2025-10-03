

statement = input("Please enter a statement: ")

values = statement.strip().split()

new_values = []
i = 0

while i < len(values):

    if values[i] == "*":
        num1 = int(values[i - 1])
        num2 = int(values[i + 1])
        result = num1 * num2
        new_values[-1] = str(result)
        i += 2


    else:
        new_values.append(values[i])
        i+=1

result = int(new_values[0])
i = 1
while i < len(new_values):

    op =  new_values[i]
    num = int(new_values[i + 1])

    if op == "+":
        result += num
        print (result)

    elif op == "-":
        result -= num
        print(result)

    elif op == "/":
        result /= num
        print(result)



    i += 2


