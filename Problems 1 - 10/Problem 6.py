# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

if __name__ == "__main__":
	sum_squares = 0
	squared_sum = 0

	for i in range(101):
		sum_squares += i ** 2
		squared_sum += i
		print(i)


	print(sum_squares)

	squared_sum = squared_sum ** 2
	print(squared_sum)

	print(squared_sum - sum_squares)