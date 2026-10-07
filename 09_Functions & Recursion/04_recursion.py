# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as function.
# Example: To find factorial of any number:
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1) # Recursive Call: Function calls itself

n = int(input("Enter a number: "))
print(f"Factorial of given number is: ",factorial(n))
