def knapsack_01(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def main():
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    print("\nEnter weight and value for each item:")
    for i in range(n):
        w = int(input(f"Weight of item {i+1}: "))
        v = int(input(f"Value of item {i+1}: "))
        weights.append(w)
        values.append(v)

    capacity = int(input("\nEnter capacity of knapsack: "))
    max_profit = knapsack_01(weights, values, capacity)
    print("\nMaximum profit in 0/1 Knapsack =", max_profit)


main()
