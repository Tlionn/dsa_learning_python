def check_for_sort(l):
    if len(l) == 0 or len(l) == 1:
        return True
    for i in range(len(l)-1):
        if l[i+1]<l[i]:
            return False
    return True

print(check_for_sort([10,10,5]))