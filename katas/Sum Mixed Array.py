'''
Sum of mixed Array

Given an array of integers as strings and numbers,
return the sum of the array values as if all were numbers.
Return your answer as a number.

'''
#By Ravishankar Chavare(GitHub:@chavarera)
def sum_mix(arr):
    return sum(map(int,arr))
    
result=sum_mix([9, 3, '7', '3'])
print(result)

'''
sum_mix([9, 3, '7', '3'])
22
sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7])
42
sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'])
41
sum_mix(['1', '5', '8', 8, 9, 9, 2, '3'])
45
'''
