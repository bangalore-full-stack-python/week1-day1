def fib(num):
	a, b = 0, 1
	while num:
		print(a)
		a, b = b, a + b
		num -= 1
		
fib(10)