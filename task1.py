import random

def objective_function(subset, target_sum):  # Funkcja celu
    return abs(sum(subset) - target_sum)

def get_neighborhood(solution, elements):  # Metoda bliskiego sąsiedztwa
    neighbor = solution[:]
    if random.random() <= 0.5 and len(neighbor) < len(elements):
        potential_elements = [e for e in elements if e not in neighbor]
        if potential_elements:
            element = random.choice(potential_elements)
            neighbor.append(element)
    elif neighbor:
        neighbor.remove(random.choice(neighbor))
    return neighbor

def generate_random_solution(elements):  # Funkcja generująca losowe rozwiązanie
    solution = []
    for element in elements:
        if random.random() > 0.5:
            solution.append(element)
    return solution

# input_elements = input("List of elements, separated by space: ")
# elements = input_elements.split()
# elements = [int(item) for item in elements]
# target_sum = int(input("Target: "))

# do testów
elements = [3, 34, 4, 12, 5, 2]
target_sum = 9

success = 0
tries = 10000
for i in range(tries):
    random_solution = generate_random_solution(elements)
    if sum(random_solution) == target_sum:
        success += 1
print(f'[RANDOM] Number of successes out of a {tries} tries: {success}')

success = 0
random_solution = generate_random_solution(elements)
for i in range(tries):
    neighborhood_solution = get_neighborhood(random_solution, elements)
    if sum(neighborhood_solution) == target_sum:
        success += 1
    random_solution = get_neighborhood(random_solution, elements)
print(f'[NEIGHBORHOOD] Number of successes out of a {tries} tries: {success}')
