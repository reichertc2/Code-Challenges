def add_binary(a,b):
    # bin() = converts numbers to its equivalent binary string
    sum = bin(a + b)
    # replace() is a method on strings requiring two arguments
    binary = sum.replace('0b','')
    return binary