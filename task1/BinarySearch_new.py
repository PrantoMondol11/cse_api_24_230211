list = [1, 2, 3, 5, 4, 6, 7, 8, 9, 0]
n = 5
pos = -1

def search(list, n):
    list.sort()  # Sorting the list for binary search
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if n > list[mid]:
                l = mid + 1
            else:
                u = mid - 1
    return False

if search(list, n):
    print("Found at position", pos + 1)
else:
    print("Not found")
