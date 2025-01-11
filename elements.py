class element:

    def twoSum(self,nums,target):
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

valu = int(input("Enter sum for which you want to make this search: "))
print("index1=%d, index1=%d" % element().twoSum((10,20,30,40,50,60,70),valu))