def is_prime(index):
    for i in range(2, index):
    	# print "i " + str(i)
        if index % i == 0:
            return False
    return True

def can_divide(n,p):
	if n%p == 0:
		return True
	return False


def largest_prime(prime):
	index = 3
	new = n
	while index<n:
		# print "index " + str(index)
		if is_prime(index) == True:
			if can_divide(new,index) == True:
				print index
				new = new/index


		index +=1
		if new == 1:
			index = n

	print "ok : "+ str(new)

n=600851475143

largest_prime(n)