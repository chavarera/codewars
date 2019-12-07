'''
Array Madness
SpeedCode #2 - Array Madness
Objective
Given two integer arrays a, b, both of length >= 1,
create a program that returns true if the sum of the squares of each element
in a is strictly greater than the sum of the cubes of each element in b.

E.g.
array_madness([4, 5, 6], [1, 2, 3]) => True
#because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
Get your timer out. Are you ready? Ready, get set, GO!!!
'''
#By Ravishankar Chavare(GitHub:@chavarera)
def array_madness(a,b):
    sum_list_a=sum(map(lambda val:val*2,a))
    sum_list_b=sum(map(lambda val:val*3,b))
    return True if (sum_list_a>sum_list_b) else False




result=array_madness([206, 1082, 849, 543, 200, 317, 1021],[11, 16, 3, 4, 24, 6, 15, 29])
print(result)
