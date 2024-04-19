def fractional_knapsack(values, weights, capacity):
    n = len(values)
    x = [0] * n
    weight = 0
    profit = 0.0

    for i in range(n):
        if weight + weights[i] <= capacity:
            x[i] = 1
            weight += weights[i]
            profit += values[i]
        else:
            x[i] = (capacity - weight) / weights[i]
            weight = capacity
            profit += values[i] * x[i]
            break

    return x, profit

# Example usage:
values = [20,40,30,50]
weights = [5,3,2,6]
capacity = 10

result, total_value = fractional_knapsack(values, weights, capacity)

print("Selected items (fractions):", result)
print("Total value:", total_value)