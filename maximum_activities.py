def maximumActivities(start, finish):
    count = 1
    time = [(start[index], finish[index]) for index in range(0, len(start))]
    time.sort()
    prev_end = time[0][1]

    index = 1

    while index < len(time):
        (start, end) = time[index]
        if (prev_end > start):
            prev_end = min(prev_end, end)
        else:
            prev_end = end
            count+=1
        index+=1
    return count
print(maximumActivities([1, 3, 2, 5], [2, 4, 3, 6]))
print(maximumActivities([1, 6, 2, 4], [2, 7, 5, 8]))

