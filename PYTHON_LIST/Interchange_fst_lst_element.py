list1 = [1,2,3,4,5,6,7,8]
print(f"before swap {list1}")
x = list1[0]
list1[0] = list1[-1]
list1[-1] = x

print(f"after swap {list1}")
