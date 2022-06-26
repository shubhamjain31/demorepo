def binary_search(lt, low, high, num):

    while low <= high:
        mid = (low + high)//2

        if num == lt[mid]:
            return mid
        elif num < lt[mid]:
            high = mid - 1
        elif num > lt[mid]:
            low = mid + 1

    return -1

lt = [12, 34, 67, 90, 93, 99]                   # worked only on sorted array
searched_element = 34
out = binary_search(lt, 0, len(lt)-1, searched_element)

if out == -1:
    print('Element Not Found')
else:
    print('Element Present At {}'.format(out+1))