def fizzbuzz(list1, list2):
    e = len(list1)
    f = len(list2)
    g = e+f 
    if g%3 == 0:
        return "fizz"
    elif g%5 == 0:
        return "buzz"
    elif g%5 == 0 and g%3 == 0:        
        return "fizzbuzz"
    
print(fizzbuzz([3, 9, 6], [4, 9]))

