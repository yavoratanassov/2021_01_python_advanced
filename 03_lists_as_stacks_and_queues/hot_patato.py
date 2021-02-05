from collections import deque

players = "George Peter Michael William Thomas".split(" ")
step = int("10")

q = deque(players)
counter = 0

while len(q) > 1:
    counter += 1
    current_player = q.popleft()
    if counter == step:
        print(f"Removed {current_player}")
        counter = 0
    else:
        q.append(current_player)

print(f"Last is {q.popleft()}")

