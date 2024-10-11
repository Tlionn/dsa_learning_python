def rm_dups(l):
    unique = []
    for x in l:
        if x not in unique:
            unique.append(x)
    return unique

print(rm_dups([10,10,20,20,30,40,40,40]))
