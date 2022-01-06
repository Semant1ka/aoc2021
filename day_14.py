from collections import defaultdict

"""
Approach:
1) For each step
2) pop each pair in current polymer
3) make an insertion, the number or times this pair repeats
4) add new pair count in the new polymer list
5) repeat the process, at the end we will have pairs with counts {"NN":100}
6) join all keys in string and use Counter to count repetitions
7) get result

"""


def get_answer(polymer, insertion_rules, steps):
    poly_1 = defaultdict(int)
    poly_2 = defaultdict(int)

    i = 0
    while i < len(polymer) - 1:
        poly_1[f"{polymer[i].strip()}{polymer[i + 1].strip()}"] += 1
        i += 1

    current = poly_1
    nxt = poly_2

    while steps > 0:
        # print(f"Current step {steps}")
        # print(f"Current pairs {current}")
        while current:
            pair, cnt = current.popitem()

            # get two new pairs
            insertion = insertion_rules[pair]

            nxt[f"{pair[0]}{insertion}"] += cnt
            nxt[f"{insertion}{pair[1]}"] += cnt

        steps -= 1

        tmp = nxt
        nxt = current
        current = tmp

    # count values

    counts = defaultdict(int)

    print(f"Final len: {sum(current.values()) + 1}")

    for kk, vv in current.items():
        counts[kk[0]] += vv
        counts[kk[1]] += vv

    for c in counts.keys():
        if c == polymer[0]:
            counts[c] += 1
        elif c == polymer[-1]:
            counts[c] += 1
        counts[c] = int(counts[c]/2)

    return max(counts.values()) - min(counts.values())


if __name__ == "__main__":
    with open("day_14_input.txt") as f:
        lines = f.readlines()

    polymer_template = lines[0].strip()

    insertion_rules = {}

    for line in lines[2:]:
        k, v = line.split('->')
        insertion_rules.update({k.strip(): v.strip()})

    print(get_answer(polymer=polymer_template, insertion_rules=insertion_rules, steps=40))
