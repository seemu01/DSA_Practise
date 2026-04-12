# longest prefix sum problem
# i/p : ["float","flowers","flow"] -> o/p : flo

def long_com_prefix(l):
    res = ""
    for i in range(len(l[0])):
        for s in l:
            if i == len(s) or s[i]!=l[0][i]:
                return res
        res += l[0][i]
    return res

l = ["float","flowers","flow"]
print(long_com_prefix(l))