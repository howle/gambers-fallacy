
# Coin Flip Simulator
This is a simple script written in Python 3.9 that simulates a coin flip to demonstrate the Gambler's Fallacy. The script flips a coin n times and tracks the following information:

Longest streak of heads or tails
   
   
   - Number of times the streak is broken
   - Total count of heads and tails
   - List of flips result

   # Usage

   ```bash
 python3.9 flip.py
 
 Longest streak:  tails
Number of times streak is broken:  9
Heads count : 472 (47.20%)
Tails count : 528 (52.80%)
flips results:  thththhtthhttthhttthhthhhtthhtthhthhhttthttththhththhhhhthhhhthtththhthhhhhhthhhhhthhththtttttththththhttthththhthhtththhththtthhhththhthtththhhthttthththhhhttthhhhttththhtthththththhttttthtthhthththhhhhtthtthtthhhttththtthhtttththhhthtttttttthhhhhttttttththhtthhthhhtttthhhhttttththtthhtthhtththtttthhhhhthhthttthhtttttthhtthhttthhttttthhtthtthhhtthtthhttthttthhhthhthhthhttthhtthtttthhthhhtttthhtttthhhththhhhhhhtththhhhtttthtttttthhthtttthtthttttttthththhhtttththtttthtthttthtthtthhhhththththhhhthhhhhhthtthththhhhttththhttthtthhththhtttthhththththtthhhthtththhhttttthhhthttththhhthtthttththhthhthttthtttthhtthhthhhhththhtthtthtttttttthhhtthhththhtthtttththhhhtthhhthttttthththhhtthhhthhtthhhthhttththhhhhhthththhttthhthtththhhtthtthtthtthttttththttthtthhthttttthhttthhththhhhthttttthhhhthhhthhthhhhthhthtthhthttthhtthttthththhttthhtthhtttttttththhthhhhththtthtthttthtththhthtttthtththtthttttttttthhthtthtththttttththtttthhthththhttthththhhhttttthhhhhthhhhhthhhhhthtthththtthttthhhthttttttthtthtth

```

   # Gambler's Fallacy

The Gambler's Fallacy, also known as the Monte Carlo Fallacy or the Fallacy of the Maturity of Chances, is the belief that the probability of an event occurring is affected by previous events or the outcome of a series of events. In the case of coin flipping, this fallacy would lead one to believe that if a coin has landed on heads several times in a row, the probability of it landing on tails on the next flip is increased. This script demonstrates that the probability of a coin landing on heads or tails is always 50-50, regardless of previous flips.

Note that this code is a simulation and is not intended for any commercial use, also the script could have been written in a more efficient way, the goal is just to illustrate the concept of the Gambler's Fallacy
