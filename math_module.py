print("Give me math problems with operations such as plus, minus, multiplication and division. For equations with these operations, add a space between each number and operator. ")
print("If want the sum of multiple numbers, then have 'sum' and the list of numbers that you want to add.")
print("If you want the average of the numbers, have 'avg' and a list of numbers you want to find the average of.")
input = input("If you want the largest number of a set of numbers then have 'max' and a list of number you want to find the largest number of (input here ->)")

if "avg" in input:
    input_list = input.split()
    input_list.remove('avg')
    int_list = [int(element) for element in input_list]
    length = int(len(input_list))
    sum = sum(int_list)
    if sum % length > 0:
        print(float(sum / length))
    elif sum % length == 0:
        print(int(sum / length))

elif "sum" in input:
    input_list = input.split()
    input_list.remove('sum')
    int_list = [int(element) for element in input_list]
    length = int(len(input_list))
    sum = sum(int_list)
    print(sum)

elif "max" in input:
    input_list = input.split()
    input_list.remove('max')
    input_list.sort()
    print(input_list[-1])

elif "+" in input:
    input_list = value.split()
    input_list.remove('+')
    print(int(input_list[0]) + int(input_list[1]))

elif "-" in input:
    input_list = value.split()
    input_list.remove('-')
    print(int(input_list[0]) - int(input_list[1]))

elif "*" in input:
    input_list = value.split()
    input_list.remove('*')
    print(int(input_list[0]) * int(input_list[1]))

elif "/" in input:
    input_list = value.split()
    input_list.remove('/')
    ele1 = int(input_list[0])
    ele2 = int(input_list[1])
    if ele1 % ele2 > 0:
        print(float(ele1 / ele2))

    elif ele1 % ele2 == 0:
	print(int(ele1 / ele2))

