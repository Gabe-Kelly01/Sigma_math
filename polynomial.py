''' Polynomials are given as a list i.e.
	2x^3 - 6x^2 + 2x - 1 = [2, -6, 2, -1]
''' 

def polynomial():
	coefficients = []
	n = int(input("Enter number of coefficients: \n"))
	print("Enter coefficients: \n")

	for i in range(0, n):
		element = int(input())
		coefficients.append(element)

	x = float(input("Value to evaluate for: \n"))

	return horner_algorithm(coefficients, n, x)

def horner_algorithm(poly, n, x):
	result = poly[0]

	'''	Algorithm handles a polynomial like a sequence of form:
					poly[1]x(n-2) + .. + poly[n-1]
	'''
	for i in range(1, n):

		result = result*x + poly[i]

	return result

def main():
	result = polynomial()
	print("Evaluated to: ", result)

main()