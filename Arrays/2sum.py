# 2 sum problem returning the index of the 2 ele's based on our target value
def two_sum(l,target):
    prevmap = {}
    for index,num in enumerate(l):
        complement = target - num
        if complement in prevmap:
            return [prevmap[complement],index]
        prevmap[num] = index
    return -1
l = [1,2,3,4,6]
target = 10
print(two_sum(l,target))