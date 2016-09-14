
#keep finding smallest, move it to the new array and remove from original
#O(n^2) - technically, O(n) * O(1/2n) but the fraction is ignored
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

def find_smallest(arr):
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i 
    return index


test_arr = [9,7,40,88,1,6,0,6,4]
print(selection_sort(test_arr))




