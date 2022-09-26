def twoSum(nums, target):
    def binarys(arr, key):
        begin = 0  # first element of list
        end = len(arr) - 1  # last element of a list
        while (end - begin > 1):
            mid = (begin + end) // 2

            if (arr[mid] == key):
                return True

            if (arr[mid] > key):
                end = mid - 1

            if (arr[mid] < key):
                begin = mid + 1

        if (arr[begin] == key) or (arr[end] == key):
            return True
        return False

    for i in nums:
        se = target - i
        if binarys(nums[nums.index(i) + 1:], se):
            first = nums.index(i)
            second = nums[first + 1:].index(se)
            return [first, second]
    return None


if __name__ == '__main__':
    print(twoSum([2, 2], 4))
