#######
#otsoy#
#######

num = int(input("Enter a number:"))

print("Amount:", num)

f1, f2 = 0, 1
count = 0


if (num) <= 0:
   new = 0

while count < num:
	new = f1 + f2
	f1 = f2
	f2 = new
	count += 1
	print(new)