nums=[5,8,3,7,1]
n = len(nums)
for i in range(1, n):
    j = i - 1
    while j >= 0 and nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
        j -= 1

#print(nums)

m = n - 1
max_num = nums[m]
second_num = nums[m - 1]
while m - 1 >= 0:
    if second_num != max_num:
        print(second_num)
        break
    else:
        m -= 1