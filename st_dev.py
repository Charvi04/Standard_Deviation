import math

# Getting the mean 
data = [60,61,65,63,98,99,90,95,91,96]

# data = [70,61,65,63,98,99,90,95,91,96]

# Finding out the mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    
    mean = total/n
    print("The value of mean is :- ",mean)
    return mean

# Squaring and getting the values
squared_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    print("The value of square is :- ", a)
    squared_list.append(a)

# Getting the sum
sum = 0
for i in squared_list:
    sum += 1

print("Summation of full list is :- ", sum)

# Dividing the sum by the total of the values
result = sum / (len(data)-1)

# Getting the sum by the total values
std_deviation = math.sqrt(result)
print("Standard Deviation is :- ",std_deviation)