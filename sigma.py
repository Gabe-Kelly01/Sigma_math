import math

def sigma():
	i = int(input("Enter lower bound of summation: \n"))
	N = int(input("Enter upper bound of summation: \n"))

	return _sigma(i, N)

def _sigma(i, N):
	''' TODO: same as integral.py, you know the thing jack'''

	# Define function to sum
	def f(x):
		return (x^2)/(x^3)

	sum = 0.0

	for k in range(i, N):
		print("Step:",k,"Sum:",sum,"\n")
		sum += f(k)

	return sum

def main():
	print("Edit function f in _sigma if needed \n")

	result = sigma()

	print("Sum of F from i to N =", result)

main()






