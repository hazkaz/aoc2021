from collections import defaultdict


def diff(a, b):
    set_a = set(a)
    set_b = set(b)
    return len(set_a.union(set_b))-len(set_a.intersection(set_b))


def decode(vals):
    groups = defaultdict(list)
    mapping = {}
    for digit in vals:
        groups[len(digit)].append(''.join(sorted(digit)))

    len_map = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }

    for key, val in groups.items():
        if key in (2, 3, 4, 7):
            mapping[''.join(sorted(val[0]))] = len_map[key]

    _235 = groups[5]
    _069 = groups[6]

    for i in range(3):
        for j in range(i+1, 3):
            if diff(_235[i], _235[j]) == 4:
                three = 3-(i+j)
                break

    mapping[_235[three]] = 3
    three_digit = _235[three]
    _235.pop(three)

    for i in range(3):
        diff_val = diff(three_digit, _069[i])
        if diff_val == 1:
            nine = i
            break

    mapping[_069[nine]] = 9
    nine_digit = _069[nine]
    _069.pop(nine)

    for digit in _235:
        diff_val = diff(digit, nine_digit)
        if diff_val == 1:
            five_digit = digit
            mapping[digit] = 5
        elif diff_val == 3:
            two_digit = digit
            mapping[digit] = 2

    for digit in _069:
        diff_val = diff(digit, five_digit)
        if diff_val == 3:
            mapping[digit] = 0
        elif diff_val == 1:
            mapping[digit] = 6

    # print(mapping)
    return mapping


counter = 0
with open('./8/input') as f:
    for line in f:
        a, b = line.strip().split(' | ')
        w, x, y, z = b.split(' ')
        mapping = decode(a.split(' '))
        print(int(''.join(str(mapping[''.join(sorted(digit))])
                          for digit in (w, x, y, z))))
        counter += int(''.join(str(mapping[''.join(sorted(digit))])
                       for digit in (w, x, y, z)))


print(counter)
