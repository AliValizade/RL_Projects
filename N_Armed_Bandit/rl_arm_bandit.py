import numpy as np

Q_table = np.zeros((5,5))

R_table = np.array([
            [1, 0.2, 2.5, 4, 1.5],
            [9, 22, 17, 10, 20],
            [1, 0.1, 3, 5, 12],
            [1.2, 0.5, 0.9, 0.7, 0.6],
            [1.5, 0.1, 0.2, 2.1, 0.7]
            ])

epsilon = 0.2
alpha = 0.1
gamma = 0.99

state = 0
active_state = {f"state {i}": 0 for i in range(5)}


print("Initial Q Table:\n", Q_table)
print("=" * 30)

for day in range(1,3001):
    tokens = 50
    while tokens > 0:
        active_state[f"state {state}"] += 1
        tokens -= 1
        random_probability = np.random.rand()
        
        best_value = np.max(Q_table[state])
        best_arm_indices = np.where(Q_table[state] == best_value)[0]
        greedy_action = np.random.choice(best_arm_indices)
        
        if random_probability >= epsilon:
            # Exploit
            action = greedy_action
        else:
            # Explore
            while True:
                action = np.random.randint(0, Q_table.shape[1])
                if action != greedy_action:
                    break
        next_state = action
        reward = R_table[state, action]
        # Q_table[state, action] += alpha * (reward - gamma * Q_table[state, action])
        max_Q_next = np.max(Q_table[next_state])
        Q_table[state, action] += alpha * (reward + (gamma * max_Q_next) - Q_table[state, action])
        state = next_state



print(f"State: {dict(active_state)}\n")

print(Q_table)

print(np.sum(Q_table))