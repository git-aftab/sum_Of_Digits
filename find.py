#Write a function to calculate the sum of digits of a given no.

#method 1 1st method by no. => string => list

def calculateSumOfDigits(x):
    Sum = 0
    string_converter = str(x)
    print(string_converter)    #checking conversion
    #list1 = string_converter.split()    # this won't work because split converts list by spaces 
    list1 = list(string_converter)
    print(list1)       ## checking conversion
    for i in list1:
        Sum+=int(i)
        print(Sum)
    return "The sum of the given digits is",Sum
a = int(input("Enter a value:"))
print(calculateSumOfDigits(a))

#method 2

def calculateSumOfDigits2(y):
    a = y%10
    print(a)
    b = y//10
    print(b)
    return f"The sum of given digits by division method is {a+b}"

intp = int(input("Enter a value:"))
print(calculateSumOfDigits2(intp))
