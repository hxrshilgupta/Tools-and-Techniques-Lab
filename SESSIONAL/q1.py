def factorial(n):
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Example usage
try:
  num = int(input("Enter a non-negative integer: "))
  result = factorial(num)
  print("The factorial of", num, "is", result)
except ValueError as e:
  print(e)