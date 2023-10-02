
# LeetCode problem # 2038. Remove Colored Pieces if Both Neighbors are the Same Color.

def winnerOfGame(colors: str) -> bool:
    # Remove the found index
    alice = 0
    bob = 0
    new_colors = ""

    for i in range(1, len(colors)-1):
        if colors[i-1] == "A" and colors[i+1] == "A" and colors[i] == "A":
            alice += 1
        if colors[i-1] == "B" and colors[i+1] == "B" and colors[i] == "B":
            bob += 1

    if alice > bob:
        return True
    elif bob > alice:
        return False

arg = "BBAAABBABBABB"

print(winnerOfGame(arg))
