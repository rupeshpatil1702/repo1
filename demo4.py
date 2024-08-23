import copy 
list1 = [10,20,30,['a','b','c']]
list2 = copy.deepcopy(list1)
print(list1,list2)
list2[-1][0] = 'aaa'
print(list1,list2)




