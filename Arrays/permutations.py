'''permutations of a given array or list in python ?
for i/p : [1,2,3] 
expected output : [1,2,3],[1,3,2],[2,3,1],[2,1,3],[3,1,2],[3,2,1] 
I am solving with recursive backtracking technique
'''
def combo(l,start=0,res = None):
    if res is None:
        res = []
    if start == len(l):
        res.append(l[:])
    for i in range(start,len(l)):
        l[start],l[i] = l[i],l[start]
        combo(l,start+1,res)
        l[start],l[i] = l[i],l[start]
    return res
l1 = [1,2,3]
print(combo(l1))

