import time
import random

def bypassbranch(subset, i):#bypass a branch
    for j in range(i-1, -1, -1):
        if subset[j] == 0:
            subset[j] = 1
            return subset, j+1

    return subset, 0

def nextvertex(subset, i, m):
    if i < m:
        subset[i] = 0
        return subset, i+1
    else:
        for j in range(m-1, -1, -1):
            if subset[j] == 0:
                subset[j] = 1
                return subset, j+1

    return subset, 0

def BB(universe, sets, costs):
    subset = [1 for x in range(len(sets))]  # all sets in
    subset[0] = 0
    bestCost = sum(costs)  # actually the worst cost
    i = 1

    while i > 0:

        if i < len(sets):
            cost, tSet = 0, set()  # t for temporary
            for k in range(i):
                cost += subset[k] * costs[k]  # if 1 adds the cost to total
                if subset[k] == 1: tSet.update(set(sets[k]))  # if 1 add the set to the cover

            if cost > bestCost:  # if the cost is larger than the currently best one, no need of further investigation
                subset, i = bypassbranch(subset, i)
                continue
            for k in range(i, len(sets)): tSet.update(set(sets[k]))
            if tSet != universe:  # that means that the set was essential at this point to complete the uni.
                subset, i = bypassbranch(subset, i)
            else:
                subset, i = nextvertex(subset, i, len(sets))

        else:
            cost, fSet = 0, set()  # f for final
            for k in range(i):
                cost += subset[k] * costs[k]
                if subset[k] == 1: fSet.update(set(sets[k]))

            if cost < bestCost and fSet == universe:
                bestCost = cost
                bestSubset = subset[:]
            subset, i = nextvertex(subset, i, len(sets))

    return bestCost, bestSubset


def generate_random_set_cover_instance(data_size) -> (set, list, list):
    universe = set(range(1, data_size + 1))
    subsets = []
    cover_set = set() 
    max_list_size = data_size // 200
    while len(subsets) < max_list_size or cover_set != universe:  
        temp_subset = sorted(list(random.sample(list(universe), random.randint(1, data_size))))
        subsets.append(temp_subset)
        cover_set.update(temp_subset)
    costs_list = [random.randint(1, 100) for _ in range(len(subsets))]
    return universe, subsets, costs_list

def main(size=None):
    if size:
        universe, subsets, costs = generate_random_set_cover_instance(size)
    else:
        print("Error: Provide a size for a randomly generated dataset.")
        return

    z = time.time()
    result = BB(universe, subsets, costs)
    cost, best_subset = result[0], result[1]
    cover = [subsets[i] for i in range(len(subsets)) if best_subset[i] == 1]
    print('covering sets:', cover, '\n', 'total cost:', cost, '$')
    print('time:', (time.time() - z)*1000)


if __name__ == '__main__':
    # Example usage:
    main(size=2000)   # For size 20
    # main(size=200)  # For size 200
    # main(size=2000) # For size 2000
