def hill_climbing_subset_sum(arr, target):
    def fitness(subset):
        return abs(target - sum(subset))

    def get_neighbors(current_subset):
        neighbors = []
        for elem in arr:
            if elem not in current_subset:
                new_subset = current_subset + [elem]
                neighbors.append(new_subset)
            else:
                new_subset = current_subset.copy()
                new_subset.remove(elem)
                neighbors.append(new_subset)
        return neighbors

    # Start with an empty subset
    current_subset = []
    current_fitness = fitness(current_subset)

    while True:
        neighbors = get_neighbors(current_subset)
        best_neighbor = min(neighbors, key=fitness)
        best_fitness = fitness(best_neighbor)

        if best_fitness >= current_fitness:
            break  # No improvement, stop the algorithm

        current_subset = best_neighbor
        current_fitness = best_fitness

    return current_subset, sum(current_subset)

# Example usage
numbers = [3, 5, 9, 2, 5]
target = 15
best_subset, best_sum = hill_climbing_subset_sum(numbers, target)
print("Best subset:", best_subset)
print("Sum of best subset:", best_sum)
