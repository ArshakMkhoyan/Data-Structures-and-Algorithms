n = int(input())
nums = list(map(int, input().split()))


def quick_sort(nums, l, r):
    if l >= r:
        return
    lt, gt = partition(nums, l, r)
    quick_sort(nums, l, lt - 1)
    quick_sort(nums, gt + 1, r)


def partition(nums, l, r):
    lt = l
    i = l
    gt = r
    pivot = nums[l]
    while i <= gt:
        if nums[i] < pivot:
            nums[lt], nums[i] = nums[i], nums[lt]
            lt += 1
            i += 1
        elif nums[i] > pivot:
            nums[gt], nums[i] = nums[i], nums[gt]
            gt -= 1
        else:
            i += 1
    return lt, gt


quick_sort(nums, 0, len(nums)-1)
print(nums)