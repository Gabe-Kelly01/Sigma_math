from math import sqrt

def quadratic():
	x_0 = float(input("Enter first coefficient: \n"))
	x_1 = float(input("Enter second coefficient: \n"))
	x_2 = float(input("Enter third coefficient: \n"))

	return PSL_quadratic(x_0, x_1, x_2)

'''
This is the Po-Shen Loh algorithm for solving a quadratic equation of form x^2 + Bx + C
'''
def PSL_quadratic(a, b, c):
	if a != 1:
		b = b/a
		c = c/a

	m = -b/2
	n = sqrt((b**2)/4 - c)

	e = m + n
	f = m - n

	if e == f:
		return e
	else:
		return e, f


def main():
	result = quadratic()
	print("The zeros of this quadratic equation are/is:", result)

main()