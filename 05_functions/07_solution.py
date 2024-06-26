def sum_all(*args): # args word is not important but the * is important
    print(args) # (1, 2) return tuple
    print(*args) # 1 2
    return sum(args)
# * means there is possible of multiple argument can come to sum_all  as a parameter

print(sum_all(1,2)) # --> 3
print(sum_all(1,2,3,4,5)) # --> 15
print(sum_all(1,2,3,4,5,6,7,8,9)) # --> 45