import time
import random

def set_cover(universe, subsets, costs):
    cost = 0
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered) / costs[subsets.index(s)])
        cover.append(subset)
        cost += costs[subsets.index(subset)]
        covered |= subset

    return cover, cost

def generate_random_set_cover_instance(size):
    universe = list(range(1, size + 1))  # Convert set to list
    num_subsets = size // 2
    subsets = [set(random.sample(universe, random.randint(1, size // 2))) for _ in range(num_subsets)]
    costs = [random.randint(1, 10) for _ in range(num_subsets)]

    print('Universe:', universe)
    print('Subsets:', subsets)
    return universe, subsets, costs




def main(size=None):
    if size:
        universe, subsets, costs = generate_random_set_cover_instance(size=size)
    else:
        print("Error: Provide a size for a randomly generated dataset.")
        return

    x = time.time()
    result = set_cover(universe, subsets, costs)

    if result is not None:
        cover, total_cost = result
        print('covering sets =', cover, '\n', 'cost =', total_cost, '$')
    else:
        print('Error: The universe is not covered by the subsets.')

    print('time:', (time.time() - x)*1000)
    print()

if __name__ == '__main__':
    # Example usage:
    main(size=2000)   # For size 20
    # main(size=200)  # For size 200
    # main(size=2000) # For size 2000
