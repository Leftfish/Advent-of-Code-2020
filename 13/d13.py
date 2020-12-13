print('Day 13 of Advent of Code!')


def check_next(timestamp, interval):
    time = ((timestamp + interval) // interval) * interval
    return interval, time - timestamp


def find_first_bus(timestamp, intervals):
    shortest = [0, 0]
    for interval in intervals:
        if interval != 'x':
            bus_id, next_arrival = check_next(timestamp, interval)
            if not shortest[1] or next_arrival < shortest[1]:
                shortest[0], shortest[1] = bus_id, next_arrival
    return shortest[0] * shortest[1]


def check_congruence(to_check, test_stamp):
    modifier = 0
    success = True
    for bus_id in to_check[1:]:
        modifier += 1
        modified_stamp = test_stamp + modifier
        if bus_id != 'x' and modified_stamp % bus_id != 0:
            success = False
            break
    return success


def find_bus_sequence(intervals):
    '''
    Just so I don't forget WTH this was all about:
    - we assume that the first element in the input is a number, not an 'x'
    - first we find the timestamp with congruence for the first two bus ids (0:end+1)
    - we do this by checking all subsequent multiples of the first element
    - once we get the result, we expand the search by one
    - we start our search at the result...
    - ...but new we jump by the multiple of all previous numbers.

    E.g. for input [2, 3, 5, 7, 11]:

    1. First we search for congruence for [2, 5], starting from 2, jump by 2
    2. We find the congruence for timestamp 2.
    3. Expand to [2, 3, 5], start from 2, now jump by 6 (2 * 3)
    4. We find the congruence for timestamp 8.
    5. Expand to [2, 3, 5, 7], start from 8, now jump by 30 (2 * 3 * 5)
    6. We find the congruence for timestamp 158.
    7. Expand to [2, 3, 5, 7, 11], start from 158, now jump by 210 (2 * 3 * 5 * 7)
    8. We find the congruence for timestamp 788, we're done.
    '''
    
    end = 1
    timestamp = intervals[0] if intervals[0] != 'x' else 1
    interval = intervals[0] if intervals[0] != 'x' else 1
    
    while end < len(intervals):
        while True:
            if not check_congruence(intervals[:end+1], timestamp):
                timestamp += interval
            else:
                if intervals[end] != 'x':
                    interval *= intervals[end]
                break
        end += 1

    return timestamp


test = '''939
7,13,x,x,59,x,31,19'''

data = test.split('\n')
timestamp = int(data[0])
intervals = [int(i) if i.isdigit() else i for i in data[1].split(',')]

print('Tests...')
print('Next ID * time to wait:', find_first_bus(timestamp, intervals) == 295)
print('First timestamp with sequence:', find_bus_sequence(intervals) == 1068781)
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    data = inp.read().split('\n')
    timestamp = int(data[0])
    intervals = [int(i) if i.isdigit() else i for i in data[1].split(',')]
    print('Next ID * time to wait:', find_first_bus(timestamp, intervals))
    print('First timestamp with sequence:', find_bus_sequence(intervals))
