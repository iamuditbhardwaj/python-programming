# We can have a value as default as default argument in a function.
# If we specify parameter = “value” in the line containing def, this value is used when no argument is passed.
# Example:
def fun(name, ending = "Thank you"): 
    gr = "Hello,"+" "+name+"\n"+ending
    return gr

n = input("Enter name: ")

print(fun(n,"Thanks"))  # Here argument is specified 
print(fun(n))   # Here argument is not specified so it will use default value