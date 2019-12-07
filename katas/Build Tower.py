'''
Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]

'''

#By Ravishankar Chavare(GitHub:@chavarera)
def tower_builder(n_floors):
    l=n_floors+n_floors-1
    result=[]
    for i in range(n_floors):
        blank=(l-(i+i+1))//2
        result.append('{}{}{}'.format(' '*blank,'*'*(i+i+1),' '*blank))
    return result

result=tower_builder(4)
print(result)

'''
['   *   ',
 '  ***  ',
 ' ***** ',
 '*******']

tower_builder(1), ['*', ]
tower_builder(2), [' * ', '***']
tower_builder(3), ['  *  ', ' *** ', '*****']
'''
