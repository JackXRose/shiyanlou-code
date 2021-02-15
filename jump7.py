for i in range(1,101):
	if i%7 == 0:
		continue
	if int(i/10)==7:
		continue
	if i-int(i/10)*10==7:
		continue
	print(i)
