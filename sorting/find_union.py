def findUnion(a, b):
        # code here
        return len(set([ele for ele in a+b]))

print(findUnion([1,2,1,1,2],[2,2,1,2,1]))