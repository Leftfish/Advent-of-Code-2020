print('Day 1 of Advent of Code!')


def find_multiple_twos(n, target):
    d = {}
    nums = list(map(int, n))

    for i in range(len(nums)):
        result = target - nums[i]
        if result in d:
            return nums[i] * nums[d[result]]
        else:
            d[nums[i]] = i
    return -1


def find_multiple_threes(n, target):
    nums = list(map(int, sorted(n)))
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while (l < r):
            if nums[i] + nums[l] + nums[r] == target:
                return nums[i] * nums[l] * nums[r]
            elif nums[i] + nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return -1

print('Tests...')
print('Multiple of a double:', find_multiple_twos(['1721', '979', '366', '299', '675', '1456'], 2020) == 514579)
print('Multiple of a triplet:', find_multiple_threes(['1721', '979', '366', '299', '675', '1456'], 2020) == 241861950)
print('---------------------')

print('Solution...')
with open('input', mode='r') as inp:
    n = [int(line.rstrip()) for line in inp]
    print('Multiple of a double:', find_multiple_twos(n, 2020))
    print('Multiple of a triplet:', find_multiple_threes(n, 2020))
