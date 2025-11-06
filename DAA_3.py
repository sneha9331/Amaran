def fractionalKnapsack(weights, values, capacity):
    n = len(weights)
    ratio = [(values[i] / weights[i], i) for i in range(n)]
    ratio.sort(reverse=True)
    total_value = 0.0
    remaining_capacity = capacity

    for r, i in ratio:
        if weights[i] <= remaining_capacity:
            total_value += values[i]
            remaining_capacity -= weights[i]
        else:
            fraction = remaining_capacity / weights[i]
            total_value += values[i] * fraction
            break
    return total_value

def main():
    n = int(input("Enter number of items: "))
    weights = []
    values = []

    print("\nEnter weight and value for each item:")
    for i in range(n):
        w = float(input(f"Weight of item {i+1}: "))
        v = float(input(f"Value of item {i+1}: "))
        weights.append(w)
        values.append(v)

    capacity = float(input("\nEnter capacity of knapsack: "))
    max_profit = fractionalKnapsack(weights, values, capacity)
    print("\nMaximum profit in knapsack = {:.2f}".format(max_profit))

main()
