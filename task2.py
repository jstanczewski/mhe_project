def subset_sum(arr, target):
    def find_subsets(arr):
        subsets = [[]]
        for elem in arr:
            new_subsets = []
            for subset in subsets:
                new_subset = subset + [elem]
                new_subsets.append(new_subset)
            subsets.extend(new_subsets)
        return subsets

    subsets = find_subsets(arr)
    # print(subsets)
    result = [subset for subset in subsets if sum(subset) == target]

    return result

# przykładowe użycie
# arr = [4, 83, 17, 42, 40, 69, 45, 76]
# target = 49

# z inputu
input_elements = input("List of elements, separated by space: ")
arr = input_elements.split()
arr = [int(item) for item in arr]
target = int(input("Target: "))
result = subset_sum(arr, target)
print(f"Podzbiory o sumie równej {target} to: {result}")
