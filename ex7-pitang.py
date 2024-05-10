def principal():
  """Main function that calls the CALC function and prints the final result."""
  # Initialize variables
  a = 0
  c = 0

  # Loop until a is less than 4
  while a < 4:
    b = calc(a)  # Call the CALC function with argument a
    c = c + b  # Add the return value of CALC to c
    a = a + 1  # Increment a

  # Print the final value of c
  print(c)

def calc(a: int) -> int:
  """Calculates a value based on the input a.

  Args:
      a: An integer value.

  Returns:
      0 if a is less than 1, 1 if a is equal to 1, or a + CALC(a-1) if a is greater than 1.
  """
  if a < 1:
    return 0
  elif a == 1:
    return 1
  else:
    return a + calc(a - 1)  # Recursive call to calc

# Call the principal function to start the program
principal()
