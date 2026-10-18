"""Perform one Q-learning update and expose its safety-relevant ingredients."""


def q_learning_update(
    old_value: float,
    reward: float,
    next_best_value: float,
    learning_rate: float,
    discount: float,
) -> float:
    """Return Q(s,a) after one temporal-difference update."""
    target = reward + discount * next_best_value
    return old_value + learning_rate * (target - old_value)


if __name__ == "__main__":
    old_q, reward, best_next_q = 1.0, -10.0, 4.0  # Collision penalty is deliberately explicit.
    updated = q_learning_update(old_q, reward, best_next_q, learning_rate=0.2, discount=0.9)
    print(f"updated Q-value: {updated:.3f}")
    print("Change the collision penalty and explain how it changes the behavior the policy is encouraged to learn.")
