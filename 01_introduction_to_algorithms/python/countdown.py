def countdown(i):
	i = float(i)
	print(i)
	if i <= 0:
		return 
		print("倒计时完毕")
	else:
		countdown(i-1)

countdown(78.2)	