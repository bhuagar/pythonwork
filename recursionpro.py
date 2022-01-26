# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""
#
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
#
#
# num = 6
# print("The factorial of", num, "is", factorial(num))




def recursionpro(n):
    if n==1:
        return 1
    else:
        return(n * recursionpro(n-1))
print(recursionpro(5))

