import random
import matplotlib.pyplot as plt

def simulate_coin_flips(n, p=0.5):
    """
    Simulates n Bernoulli trials with success probability p.
    Returns a list of running means.
    """
    heads = 0
    running_means = []

    for i in range(1, n + 1):
        if random.random() < p:
            heads += 1
        running_means.append(heads / i)

    return running_means


def main():
    n = 5000
    p = 0.5
    trials = 3

    for _ in range(trials):
        means = simulate_coin_flips(n, p)
        plt.plot(means, alpha=0.8)

    plt.axhline(p, linestyle="--")
    plt.xlabel("Number of trials")
    plt.ylabel("Running mean")
    plt.title("Law of Large Numbers (Coin Flips)")
    plt.show()


if __name__ == "__main__":
    main()
