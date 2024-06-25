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

    return dp[arr_len][target_sum]


# Przykładowe użycie:
# arr = [3, 4, 5]
# T = 9

input_elements = input("List of elements, separated by space: ")
arr = input_elements.split()
arr = [int(item) for item in arr]
target_sum = int(input("Target: "))

print(subset_sum(arr, target_sum))
