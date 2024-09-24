def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1  # Not enough total gas to cover total cost

    start = 0
    tank = 0
    total_tank = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        total_tank += gas[i] - cost[i]

        if tank < 0:
            # If tank is negative, we cannot start from `start` to `i`
            # So, we set `start` to `i + 1` and reset `tank`
            start = i + 1
            tank = 0

    return start if total_tank >= 0 else -1

# Example usage:
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
start_station = can_complete_circuit(gas, cost)
print("The starting gas station index is:", start_station)