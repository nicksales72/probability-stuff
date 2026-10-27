import random 

"""
Question: 
    Suppose an urn contains 8 red balls and 4 white balls. We draw two balls without replacement. What is the probability that both are red?

Solution: 
    R1: Event that the first ball is red.
    R2: Event that the second is red.

    P(R1) = 8/12; P(R2 | R1) = 7/11
    P(R1 ∩ R2) = P(R1)P(R2 | R1) = (8/12)(7/11) = 14/33
"""

def draw_balls(urn):
    return urn.pop(random.randint(0,len(urn)-1))

def both_red(trials):
    total_both_red = 0
    for i in range(trials):
        urn = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'w', 'w', 'w', 'w']
        if draw_balls(urn) == 'r' and draw_balls(urn) == 'r': total_both_red += 1
    return total_both_red / trials

print(f"Empirical = {both_red(10000000):.3f}\n14/33 = {14/33:.3f}")
