import random

n_trials = 100_000
rng = random.Random(42)  # Makes the results repeatable


def run_trial():
    """Simulate one experiment."""
    die_1 = rng.randint(1, 6)
    die_2 = rng.randint(1, 6)

    return die_1 + die_2


successes = 0

for _ in range(n_trials):
    result = run_trial()

    if result >= 10:
        successes += 1

probability = successes / n_trials

print(f"Estimated probability: {probability:.2%}")