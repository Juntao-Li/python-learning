nums = [3,1,4,1,5]
print(nums)

# 排序
sorted_nums = sorted(nums)
print(sorted_nums)

# 去重
unique_nums = list(set(nums))
print(unique_nums)

# 找最大值
max_nums = max(nums)
print(max_nums)

# 找第二大
second_nums = sorted(set(nums))[-2]
print(second_nums)

# 切片
print(nums[:2])
print(nums[::2])
print(nums[3:])

# 列表推导式
squares = [x ** 2 for x in nums]
print(squares)

#偶数
evens = [x for x in nums if x % 2 == 0]
print(evens)