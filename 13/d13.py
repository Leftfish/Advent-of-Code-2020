print('Day 13 of Advent of Code!')


def check_next(timestamp, interval):
    time = ((timestamp + interval) // interval) * interval
    return (interval, time - timestamp)


def find_first_bus(timestamp, intervals):
    shortest = [float('inf'), float('inf')]
    for interval in intervals:
        bus_id, next_arrival = check_next(timestamp, interval)
        if next_arrival < shortest[1]:
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


def check(intervals):
    end = 1
    result = intervals[0] if intervals[0] != 'x' else 1
    interval = intervals[0] if intervals[0] != 'x' else 1
    
    while end < len(intervals):
        while True:
            if not check_congruence(intervals[:end+1], result):
                result += interval
            else:
                if intervals[end] != 'x':
                    interval *= intervals[end]
                break
        end += 1

    return result


test = '''939
7,13,x,x,59,x,31,19'''

data = test.split('\n')
timestamp = int(data[0])
intervals = [int(i) for i in data[1].split(',') if i.isdigit()]
all_intervals = [int(i) if i.isdigit() else i for i in data[1].split(',')]

print('Tests...')
print('Next ID * time to wait:', find_first_bus(timestamp, intervals) == 295)
print('First timestamp with sequence:', check(all_intervals) == 1068781)
print('---------------------')

with open('input', mode='r') as inp:
    print('Solution...')
    data = inp.read().split('\n')
    timestamp = int(data[0])
    intervals = [int(i) for i in data[1].split(',') if i.isdigit()]
    all_intervals = [int(i) if i.isdigit() else i for i in data[1].split(',')]
    print('Next ID * time to wait:', find_first_bus(timestamp, intervals))
    print('First timestamp with sequence:', check(all_intervals))
