def maximumMeetings(start, end):
    # Start, End, JobID
    meetings = [(start[index], end[index], index + 1) for index in range(len(start))]
    # Sort by Start times
    meetings.sort()
    result = []

    prev_end = -1

    for (start_time, end_time, id) in meetings:
        # if next start time is > or = then its a collision 
        if (prev_end > start_time):
            # if end times are same and previous result has lower job id then consider it - as per question
            # or if end_time of current activity falls with in the previous range
            if (end_time == prev_end and result[-1] > id) or (end_time < prev_end):
                result.pop()
                result.append(id)
                prev_end = min(prev_end, end_time)
        else:
            prev_end = end_time
            result.append(id)
    return result
print(maximumMeetings([1,3,0,5,8,5], [2,4,6,7,9,9])) # 1 2 4 5
print(maximumMeetings([0 ,7, 1, 4, 8], [2, 9 ,5 ,9, 10]))

