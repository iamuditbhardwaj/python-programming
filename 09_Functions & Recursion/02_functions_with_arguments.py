# A function can accept some value it can work with. We can put these values in the parentheses.

def greet_1(name): # (name) is the parameter
    gr = "Hello,"+" "+name
    return gr   # returns the value of gr 

n = input("Enter a name: ")
print(greet_1(n)) # return value of gr is in n

# A function can also have multiple arguments
def greet_2(name,wish,ending): # name, wish, ending are multiple parameters in single funtion
    gr = "Hello,"+" "+name+"\n"+wish+"\n"+ending
    return gr

n = input("Enter name: ")
w = input("Enter a message: ")
print(greet_2(n,w,"Thank you"))
