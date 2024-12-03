# pair up the numbers, how far apart are they?
# pair up smallest num in left, with smallest num in right
# then second smallest on each side, etc.
# for each pair, calc how far apart they are
# then add up all of those distances


def get_input():
    with open("day1.txt", "r") as f:
        return f.readlines()


left = []
right = []
for line in get_input():
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))
sum = 0
while len(left) > 0:
    l_min = min(left)
    r_min = min(right)
    left.remove(l_min)
    right.remove(r_min)
    sum += abs(r_min - l_min)
print(sum)
