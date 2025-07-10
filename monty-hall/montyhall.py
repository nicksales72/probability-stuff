import sys
import random
import numpy as np 
import matplotlib.pyplot as plt

def monty_hall(strat: str, trials: int) -> float:
    wins = 0 
    for _ in range(trials):
        doors = [0, 1, 2]
        car_door = random.choice(doors)
        player_choice = random.choice(doors)

        possbile_doors = [x for x in doors if x != player_choice and x != car_door]
        monty_open_choice = random.choice(possbile_doors)

        if strat == "switch":
            remaining_doors = [x for x in doors if x != player_choice and x != monty_open_choice]
            player_final_choice = remaining_doors[0]
        else:
            player_final_choice = player_choice

        if player_final_choice == car_door:
            wins += 1
    
    return wins / trials

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 montyhall.py <number_of_traisl>")
        sys.exit(1)

    try:
        trails = int(sys.argv[1])
    except ValueError:
        print("<number_of_trails> must be an integer")
        sys.exit(1)

    win_rate_stay = monty_hall("stay", trails)
    win_rate_switch = monty_hall("switch", trails)

    print(f"Win rate when staying: {win_rate_stay:.4f}")
    print(f"Win rate when switching: {win_rate_switch:.4f}")

    x = np.array(["Stay", "Switch"])
    y = np.array([win_rate_stay, win_rate_switch])

    plt.bar(x, y)
    plt.show(block=False)
    plt.pause(10)