# 1. You are free to use anything we've studied till now.
# 2. The number of guesses should be limited, i.e (5 or 9).
# 3. Print the number of guesses left.
# 4. Print the number of guesses he took to win the game.
# 5. “Game Over” message should display if the number of guesses becomes equal to 0.
# You are advised to participate in solving this problem.
# This task helps you become a good problem solver and helps you accept the challenge and acquire new skills.

n = 56
choice = 1
while(True):
    g_left = 9 - choice
    if g_left >= 0:
        print("Enter your guess no.",choice,"You've total 9 guesses to reach the hidden number between 1 to 100.")
        guess = int(input())
        if guess < n:
            print("No, the hidden number is greater.")
            print(g_left, "guesses left")
            choice += 1
            continue
        elif guess > n:
            print("No, the hidden number is smaller.")
            print(g_left, "guesses left")
            choice += 1
            continue
        else :
            print("Congrats!, your guess is correct and the hidden number is",n)
        break
    else :
        break

print("Sorry, you have no guesses left, GameOver.")

