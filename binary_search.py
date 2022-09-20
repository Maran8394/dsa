import random

def binary(li, el):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high)//2
        
        find_el = li[mid]
        if find_el == el:
            return mid
        elif find_el > el:
            high = mid -1
        else:
            low = mid +1
    return
li = [i for i in range(100)]
k = random.sample(range(2,2000),40)
k.sort()

print(k[10],"EL")
d = binary(k,k[10])
if d:
    print("Find --->",k[d])
else:
    print("Not Found")

