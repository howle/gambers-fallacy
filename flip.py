import random

# Number of coin flips
n = 1000

# Number of times heads or tails appears in a row
streak = 0

# Current streak of heads or tails
current_streak = ""

# Longest streak of heads or tails
longest_streak = ""

# Number of times the streak is broken
streak_breaks = 0

# Total count of heads and tails
heads_count = 0
tails_count = 0

# list to store all the flips result
flips_result = []

# Flip a coin n times
for i in range(n):
    coin = random.choice(["heads", "tails"])
    flips_result.append(coin[0])
    # Check if the current flip is heads
    if coin == "heads":
        heads_count += 1
    else:
        tails_count += 1
    # Check if the current flip continues the current streak
    if coin == current_streak:
        streak += 1
    else:
        # Check if the current streak is longer than the previous longest streak
        if streak > streak_breaks:
            streak_breaks = streak
            longest_streak = current_streak
        streak = 1
        current_streak = coin

print("Longest streak: ", longest_streak)
print("Number of times streak is broken: ", streak_breaks)
print(f"Heads count : {heads_count} ({(heads_count/n)*100:.2f}%) ")
print(f"Tails count : {tails_count} ({(tails_count/n)*100:.2f}%) ")
print("flips results: ", ''.join(flips_result))
