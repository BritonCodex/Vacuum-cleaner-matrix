import random

def display(room):
    for row in room:
        print(row)

# Initialize a 4x4 room with all 1s (dirty)
room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

print("All the rooms are dirty:")
display(room)

# Randomize dirt (0: clean, 1: dirty)
for x in range(4):
    for y in range(4):
        room[x][y] = random.choice([0, 1])

print("\nBefore cleaning, the robot detects random dirt:")
display(room)

# Clean the room
z = 0  # count of cleaned dirty rooms
for x in range(4):
    for y in range(4):
        if room[x][y] == 1:
            print(f"Vacuuming location ({x},{y})")
            room[x][y] = 0
            print(f"Cleaned ({x},{y})")
            z += 1

print("\nRoom is cleaned now. Thanks for using: 3710933")
display(room)

performance = (z / 16) * 100
print(f"Performance: {performance:.2f}%")
