def sum_fibonacci_not_even():
	fib = [1,1]
	total = 0
	while fib[-1]<4000000:
		to_add = fib[-1]+fib[-2]
		fib.append(to_add)
		if not fib[-1] % 2:
			total+=to_add
	fib[-1] = 0
	print fib
	return total

print sum_fibonacci_not_even()w