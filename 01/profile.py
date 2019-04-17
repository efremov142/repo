first_name = input("Enter your First name: ")
second_name = input("Enter your Second name: ")
age = int(input("Enter your age: "))
print(first_name + " " + second_name + ", ", end="")
if age <= 5:
	print("you are too young")
elif age < 11:
	print("you are in primary school")
elif age < 16:
	print("you are in secondary school")
elif age < 19:
	print("you are in high school")
else:
	print("you are too old")
