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
coin_flips_result = {"H": 0, "T": 0}

# flips results
flips_result = [ "H" if random.choice(["heads", "tails"]) == "heads" else "T" for i in range(n)]

# Flip a coin n times
for coin in flips_result:
    coin_flips_result[coin] +=1
    if coin == current_streak:
        streak += 1
    else:
        if streak > streak_breaks:
            streak_breaks = streak
            longest_streak = current_streak
        streak = 1
        current_streak = coin

heads_percentage = (coin_flips_result["H"]/n)*100
tails_percentage = (coin_flips_result["T"]/n)*100
print("Longest streak: ", longest_streak)
print("Number of times streak is broken: ", streak_breaks)
print(f"Heads count : {coin_flips_result['H']} ({heads_percentage:.2f}%) ")
print(f"Tails count : {coin_flips_result['T']} ({tails_percentage:.2f}%) ")
print("flips results: ", ''.join(flips_result))
