n, *nums1 = list(map(int, input().split()))
k, *nums2 = list(map(int, input().split()))


def binary_search(p, nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == p:
            return mid
        elif nums[mid] > p:
            r = mid - 1
        else:
            l = mid + 1
    return -1


res = []
for i in range(k):
    res.append(binary_search(nums2[i], nums1))

print(res)

