time = []
value = []

x = []
y = []
# with open("time.txt") as f:
#     for line in f:
#         time.append(float(line))

# with open("value.txt") as f:
#     for line in f:
#         value.append(float(line))

# with open("time_value.txt", "w+") as f:
#     for t, v in zip(time, value):
#         f.write(f"{t}, {v}\n")

with open("time_value.txt") as f:
    for line in f:
        x_, y_ = line.split(',')
        x.append(x_)
        y.append(y_)

for x_, y_ in zip(x, y):
    print(f"{float(x_)}, {float(y_)}")



