from module_a import randfun 

size = 10
numbers = randfun(size)

# calculating max of the sequence
def printMax(numbers):
    max = numbers[0]
    for x in randfun(size):

        if x > max :
            max = x
    
    return str(max)

# calculating min of the sequence
def printMin(numbers):
    min = numbers[0]
    for x in randfun(size):
        if x < min :
            min = x
    
    return str(min)

# calculating average of the sequence
def getAvrg(numbers):
    sum = 0
    for x in randfun(size): 
        sum = sum + x

    return sum / size

# calculating average of the sequence
def variation(numbers):
    avrg = getAvrg(numbers)
    sum = 0
    for x in numbers : 
        x = x - avrg
        x = x * x 
        sum = sum + x

    return sum / size

print(variation(numbers))
