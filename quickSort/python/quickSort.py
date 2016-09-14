from random import randint
#O(n log n) on average; O(n^2) in the worst case
#In averate there are O(log n) levels (split the array) and 
#each level takes O(n) (touch each element in array)
#Worst case ()
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0] #this needs to be random
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort([98,77,33,1,8,4,99,4,10]))