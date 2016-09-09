data = [1,4,6,9,21,65]

def binary_search(items, item):
    low = 0
    high = len(items) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) / 2
        guess = items[mid]
        if (guess == item):
            return (mid,count)
        elif (item < guess):
            high = mid - 1
        else:
            low = mid + 1
    return (None,count)

def test():
    index = binary_search(data,65)
    print(index)

test()

    