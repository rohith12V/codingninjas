def jobScheduling(jobs):
    prices = []
    max_deadline = 0
    for x_index in range(0, len(jobs)):
        prices.append([jobs[x_index][1], jobs[x_index][0]])
        max_deadline = max(max_deadline, jobs[x_index][0])
    prices.sort(reverse=True)
    profit = 0
    # Slots to be filled up
    positions = [False for _ in range(max_deadline)]

    for index, (price, deadline) in enumerate(prices):
        deadline -= 1
        # get first non occupied slot
        while deadline > 0 and positions[deadline]:
                deadline-=1

        # if slot is free and our deadline is still there
        if not positions[deadline]:
            positions[deadline] = True
            profit += price
    return profit 

print(jobScheduling(
    [
        [2, 25],
        [4, 40],
        [4, 39],
        [1, 5],
        [3, 50],
        [5, 60]
    ]
))