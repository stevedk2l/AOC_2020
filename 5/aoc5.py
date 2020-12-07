
with open("input", 'r') as f:
    data = f.readlines()


def calculate(line):
    row = find_row(0, 127, line[0:7], 0)
    col = find_row(0, 7, line[7::], 0)

    return (row * 8) + col


def find_row(floor, ceil, string, letter):

    if floor == ceil:
        return floor

    pivot = (ceil - floor) // 2
    if string[letter] == "F" or string[letter] == "L":
        letter += 1
        return find_row(floor, floor + pivot, string, letter)

    if string[letter] == "B" or string[letter] == "R":
        letter += 1
        return find_row(ceil - pivot, ceil, string, letter)


ids = [calculate(line) for line in data]
ids.sort()
print(ids[-1])

my_seat = [x for x in range(ids[-1]) if x not in ids and x > ids[0]]
print(my_seat[0])