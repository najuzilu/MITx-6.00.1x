# Python 3

def genPrimes():
	'''	Yield primes and store previous primes in array
		Number x is a prime if (x % p) != 0	
	'''
	prime = 2
	prime_array = []

	while True:
		if len(prime_array) == 0:
			prime_array.append(prime)
			yield prime
			prime += 1
		else:
			if all(prime % x != 0 for x in prime_array):
				prime_array.append(prime)
			if prime == prime_array[-1]:
				yield prime
			prime += 2

if __name__ == '__main__':
	a = genPrimes()
	print(a.__next__())
	print(a.__next__())
	print(a.__next__())
	print(a.__next__())
	print(a.__next__())
