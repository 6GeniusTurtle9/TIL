def binary_search(element, some_list):
    start, mid, last = 0, len(some_list)//2, len(some_list)-1
    while start != last :
        mid = (start+last)//2
        if element == some_list[mid]:
            return mid
        elif element < some_list[mid]:
            last = mid
        else:
            start = mid
        if start == last:
            return 'None'
        
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))