import math

def integrate(auto_bound = False):
	# Get inputs for helper function
	if auto_bound:
		N = 10_000
	else:
		N = int(input("Enter upper index of summation: \n"))

	a = float(input("Enter lower bound of integration: \n"))
	b = float(input("Enter upper bound of integration: \n"))

	return _integrate(N, a , b)

def _integrate(N, a, b):

	'''
	TODO find a way for user to enter f without touching code,
	clears way for a GUI implementation  later
	'''

	# Define the function to integrate as f
	def f(x):
		return math.sin(x)/(math.cos(x)+1)

	sum = 0

	for n in range(1, N+1):
		sum += f(a + ((n-(1/2)) * ((b-a)/N)))

	return sum * ((b-a)/N)

def main():
	print("Edit function f in _integrate if needed")
	auto = input("Enter y for arbitrarily large bound on summation \n")

	if auto:
		result = integrate(auto_bound = True)
	elif not auto:
		result = integrate(auto_bound = False)

	print("Integral of f = ", result, "(approximation)")

main()


