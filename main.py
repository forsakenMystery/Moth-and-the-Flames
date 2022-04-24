import numpy as np

size = 5  # should be odd
actions_name = {
    0: "nothing",
    1: "right",
    2: "left",
    3: "up",
    4: "down"
}
action_probability = [0.1, 0.225, 0.225, 0.325, 0.125]
actions_move = {
    0: (-0, +0),
    1: (-0, +1),
    2: (+0, -1),
    3: (-1, +0),
    4: (+1, -0)
}
room = np.zeros(shape=(size, size), dtype=np.int8)
print(room)
light = (0, size//2)
room[light] = 1
print(room)
moth = (np.random.randint(0, size), np.random.randint(0, size))
while(moth[0] == light[0] and moth[1] == light[1]):
    moth = (np.random.randint(0, size), np.random.randint(0, size))
print(moth)
room[moth] = 2
print(room)
door_size = 3
i = 0
while(i < door_size):
    room[size-i-1, size-1] = 3
    i += 1
print(room)
if(light[1]-moth[1] < 0):
    action_probability[1] -= 0.1
    action_probability[2] += 0.1
elif(light[1]-moth[1] > 0):
    action_probability[1] += 0.1
    action_probability[2] -= 0.1
print(room)
print(action_probability)
direction = np.random.choice(5, 1, p=action_probability)[0]
print(direction)
print(actions_move[direction])
