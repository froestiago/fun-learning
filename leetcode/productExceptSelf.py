nums = [1, 2, 3, 4]
#output should be [24, 12, 8, 6]


def productExceptSelfWithDivision(nums):
    totalProduct = 1
    output = []
    for i in nums:
        totalProduct = totalProduct*i
    for i in nums:
        output.append(totalProduct/i)

    return output

def productExceptSelfNotGood(nums):
    output = []
    n = len(nums)

    for i in range(n):
        leftProduct = 1
        rightProduct = 1
        #left product
        x = 0
        while x < i:
            leftProduct *= nums[x]
            x += 1
        #right product
        y = i+1
        while y < n:
            rightProduct = rightProduct * nums[y]
            y += 1
        totalProduct = leftProduct * rightProduct
        output.append(totalProduct)
    return output

def productExceptSelf(nums):
    output = []
    n = len(nums)
    leftProduct, righProduct = [1], [1]
    i=1
    while i < n:
        leftProduct.append(leftProduct[i-1] * nums[i-1])
        righProduct.append(righProduct[i-1]* nums[n-i])
        i += 1
    righProduct = righProduct[::-1]
    for x, y in zip(leftProduct, righProduct):
        output.append(x*y)
    return(output)


print(productExceptSelf(nums))

#print(productExceptSelfWithDivision(nums))