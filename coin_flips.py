import random

def get_inputs() -> int:
    return int(input("Enter number of flips: "))

def simulate_flips(num: int) -> tuple[int, int]:
    heads = sum(random.random() < 0.5 for _ in range(num))
    return (heads, num - heads)

def display_results(num_flips: int, heads: int, tails: int):
          print(f"Heads: {heads/num_flips:.2f}, Tails: {tails/num_flips:.2f}")

def main():
    num_flips = get_inputs()
    heads, tails = simulate_flips(num_flips)
    display_results(num_flips, heads, tails)

if __name__ == "__main__":
    main()
