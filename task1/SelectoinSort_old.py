def sort (nums):
    for i in range (len(nums)-1):
        min=i
        for j in range (i+1,len(nums)):
            if nums[j]<nums[min]:
                min=j
                nums[i],nums[min]=nums[min],nums[i]





nums=[1,2,3,2,43,5,3,4,6,8]
sort(nums)
print(nums)