import numpy as np
def american_option(S0, K, r, T, n, u, d, option_type="call"):
    # Calculate parameters
    delta_t = T / n
    p = (np.exp(r * delta_t) - d) / (u - d)  # Risk-neutral probability
    discount = np.exp(-r * delta_t)  # Discount factor

    # Option values at maturity
    option_values = []
    for i in range(n + 1):
        stock_price = S0 * (u ** i) * (d ** (n - i))
        if option_type == "call":
            option_values.append(max(stock_price - K, 0))
        else:  # Put option
            option_values.append(max(K - stock_price, 0))

    # Backward induction
    for step in range(n - 1, -1, -1):
        for i in range(step + 1):
            stock_price = S0 * (u ** i) * (d ** (step - i))
            hold_value = discount * (p * option_values[i + 1] + (1 - p) * option_values[i])
            if option_type == "call":
                exercise_value = max(stock_price - K, 0)
            else:
                exercise_value = max(K - stock_price, 0)
            option_values[i] = max(hold_value, exercise_value)

    return option_values[0]

# Example Parameters
S0 = 100  # Stock price
K = 105  # Strike price
r = 0.05  # Risk-free rate
T = 1  # Time to maturity
n = 2  # Steps
u = 1.2  # Up factor
d = 0.8  # Down factor

# Compute prices
call_price = american_option(S0, K, r, T, n, u, d, option_type="call")
put_price = american_option(S0, K, r, T, n, u, d, option_type="put")

print(f"Call Option Price: {call_price:.2f}")
print(f"Put Option Price: {put_price:.2f}")
