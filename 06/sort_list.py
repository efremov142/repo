def print_list(lst):
	for i in range(len(lst)):
		el = lst[i]
		print(el, end=' ')
	print()
l = [9, 8, 7, 6, 5]
# print_list(l)	
# print_list([7, 4, 3, 2, 1])

def print_list2(lst):
	for el in lst:
		print(el)
# print_list2(l) 

def sort_list(lst):
	return sorted(lst)
print_list(l)
l = sort_list(l)
print_list(l)