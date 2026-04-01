# running sum problem solving with python basic arrays

def RunningSum(nums):
  sum = 0
  res = []
  for i in nums:
    sum += i
    res.append(sum)
  return res
# here we can declare one array and can call the function
arr = [1,2,3,4]
print(RunningSum(arr))

    
