print('Day 9 of Advent of Code!')


def find_twos(nums, target):
    d = {}
    for i in range(len(nums)):
        result = target - nums[i]
        if result in d:
            return nums[i], nums[d[result]]
        else:
            d[nums[i]] = i
    return 0


def find_invalid(data, chunk_size):
    for i in range(chunk_size+1, len(data)):
        start, stop, target = i-chunk_size-1, i-1, i-1
        if not find_twos(data[start:stop], data[target]):
            return data[target]
    return 0


def find_subarray(data, target):
    current_sum = data[0]
    start = 0
    for end in range(1, len(data)):
        while current_sum > target and start < end-1:
            current_sum -= data[start]
            start += 1
        if current_sum == target:
            result = data[start:end]
            return max(result) + min(result)
        current_sum += data[end]
    return 0

test_data = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

data = [int(i) for i in test_data.split()]

print('Tests...')
print('Invalid number:', find_invalid(data, 5) == 127)
print('Encryption weakness:', find_subarray(data, 127) == 62)
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    data = [int(i) for i in inp.readlines()]
    invalid = find_invalid(data, 25)
    print('Invalid number: {}'.format(invalid))
    print('Encryption weakness: {}'.format(find_subarray(data, invalid)))
