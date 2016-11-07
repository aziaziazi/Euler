def try_3_5():
	count = 1
	inside = []
	while count<1000:
		if count%3==0:
			inside.append(count)
		if count%5==0:
			if count!=inside[-1]:
				inside.append(count)
		count+=1
	return sum(inside)

print try_3_5()

