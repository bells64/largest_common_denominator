num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
while not num1 == num2:
	if num1 > num2:
		num1 = num1 - num2
	else: 
		num2 = num2 - num1
print(num2)	