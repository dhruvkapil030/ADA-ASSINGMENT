
def fractional_knapsack(w, v, capacity):
    ratio = sorted([(v[i]/w[i], w[i], v[i]) for i in range(len(w))], reverse=True)
    total = 0
    for r, weight, value in ratio:
        if capacity >= weight:
            capacity -= weight
            total += value
        else:
            total += r * capacity
            break
    return total


def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    result = [activities[0]]
    for i in activities[1:]:
        if i[0] >= result[-1][1]:
            result.append(i)
    return result


import heapq

def huffman(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0]+hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda x: x[0])


print("Knapsack:", fractional_knapsack([10,20,30],[60,100,120],50))
