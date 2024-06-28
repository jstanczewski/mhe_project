import random

def subset_sum(arr, target_sum):
    arr_len = len(arr)

    # Tablica gdzie dp[i][j] == True, jeśli istnieje podzbiór pierwszych i elementów, który sumuje się do j
    dp = [[False] * (target_sum + 1) for _ in range(arr_len + 1)]

    # Podzbiór sumujący się do 0 zawsze istnieje (pusty podzbiór)
    for i in range(arr_len + 1):
        dp[i][0] = True

    # Wypełnianie tablicy
    for i in range(1, arr_len + 1):
        for j in range(1, target_sum + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    # Odtworzenie podzbioru, który tworzy tę sumę
    result = []
    i, j = arr_len, target_sum
    while i > 0 and j > 0:
        if dp[i - 1][j]:
            i -= 1
        else:
            result.append(arr[i - 1])
            j -= arr[i - 1]
            i -= 1
    is_sum_possible = dp[arr_len][target_sum]
    return is_sum_possible, result


def closest_subset_sum(arr, target_sum):
    arr_len = len(arr)

    dp = [[False] * (target_sum + 1) for _ in range(arr_len + 1)]
    closest = [0] * (target_sum + 1)
    print(closest)

    for i in range(arr_len + 1):
        dp[i][0] = True

    for i in range(1, arr_len + 1):
        for j in range(1, target_sum + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
                if dp[i][j]:
                    closest[j] = max(closest[j], j)
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                if dp[i][j]:
                    closest[j] = max(closest[j], j)
    print(closest)

    # znalezienie najbliższej sumy
    best_sum = 0
    for j in range(target_sum + 1):
        if dp[arr_len][j]:
            best_sum = max(best_sum, closest[j])

    result = []
    i, j = arr_len, best_sum
    while i > 0 and j > 0:
        if dp[i - 1][j]:
            i -= 1
        else:
            result.append(arr[i - 1])
            j -= arr[i - 1]
            i -= 1

    return best_sum, result

def random_subset(arr):
    random_subset = [x for x in arr if random.choice([True, False])]
    return random_subset


# przykładowe użycie
# arr = [3, 4, 6, 10]
# target_sum = 12

# z inputu
input_elements = input("List of elements, separated by space: ")
arr = input_elements.split()
arr = [int(item) for item in arr]
target_sum = int(input("Target: "))

is_sum_possible, result = subset_sum(arr, target_sum)
random_subset = random_subset(arr)
print(f"Czy suma {target_sum} jest osiągalna: {is_sum_possible}")
if is_sum_possible:
    print(f"Elementy: {result}")
else:
    best_sum, elements = closest_subset_sum(arr, target_sum)
    print(f"Najbliższa suma: {best_sum}, Elementy tworzące tę sumę: {elements}")
print(f"Losowy zbiór: {random_subset}, suma: {sum(random_subset)}")
