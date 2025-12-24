import numpy as np
import matplotlib.pyplot as plt

def value_gambler(p_h, theta=0.00009, goal=100):
    v = np.zeros(goal+1)
    v[goal] = 1
    
    states = range(1, goal)
    
    while True:
        delta = 0
        for s in states:
            v_old = v[s]
            actions = range(1, min(s, goal-s) + 1)
            action_values = []

            for a in actions:
                # Belman formula (R = 0, gamma = 1)
                v_next = p_h * v[s + a] + (1 - p_h) * v[s - a]
                action_values.append(v_next)

            v[s] = max(action_values)
            delta = max(delta, abs(v_old - v[s]))

        if delta < theta:
            break
    
    # Update Policy
    policy = np.zeros(goal + 1)
    for s in states:
        actions = range(1, min(s, goal-s) + 1)
        action_values = []
        
        for a in actions:
            q_sa = p_h * v[s + a] + (1 - p_h) * v[s - a]
            action_values.append(q_sa)

        policy[s] = actions[np.argmax(action_values)]

    return v, policy


v_25, pi_25 = value_gambler(p_h=0.25)
v_55, pi_55 = value_gambler(p_h=0.55)

# Plot
plt.figure(figsize=(15, 4))

# v plot
plt.subplot(1, 3, 1)
plt.plot(v_25[:100], label='p_h = 0.25')
plt.plot(v_55[:100], label='p_h = 0.55')
plt.title('Value function')
plt.xlabel('Capital')
plt.ylabel('Value Estimates')
plt.legend()
plt.grid()

# pi = 0.25
plt.subplot(1, 3, 2)
plt.bar(range(100), pi_25[:100], align='center')
plt.title('Optimal Policy (p_h = 0.25)')
plt.xlabel('Capital')
plt.ylabel('Optimal Bet')

# pi = 0.55
plt.subplot(1, 3, 3)
plt.bar(range(100), pi_55[:100], align='center')
plt.title('Optimal Policy (p_h = 0.55)')
plt.xlabel('Capital')
plt.ylabel('Optimal Bet')

plt.tight_layout()
plt.show()

