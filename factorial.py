

num = int(input("Enter a number: "))

def factorial1(num):
	if num == 0:
		return 1

	f = 1
	i = 0
	
	while i < num:
		i += 1
		f = f * i
	return f


print("The factorial of ", num, " is : ")
print(factorial1(int(num)))
