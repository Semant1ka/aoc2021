
"""
Example Input:
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe

1: be
8: cfbegad, fdgacbe # not helpful because it contains all values anyway
7: edb
0-6-9: cbdgef, fgaecd, agebfd
4: cgeb
2-3-5: fdcge, fecdb, fabcd

# sort all of them lexicographically
_ _ _ _ _ _ _
a b c d e f g

1:be
8:abcdefg
7:bde
4:becg
0-6-9:bdefg, acdefg, abdefd - a,d,g -> f,d,c +
2-3-5:cdefg, bcdef, abcdf - 3 common latters are a,d,g -> f,d,c /

1. find set of horizontal letters
2. find d from 4 intercection with f,d,c from 2-3-5 -> becg/f,d,c -> g => d == c
3. find a from 7 intersection with f,d,c - c -> bde/f,d -> a == d
# so far we found aaaa and dddd
4. that means that g == f

5.find c and f by intersecting 1 and 7; bde/be => cf = be
6. among 2-3-5 find one that intersects with be, remove dcf first -> bcdef is number 3
7. now the rest of the digits a and g are b and e respectively
8. now take number 3 bcdef and 4 becg, remove top and bottom from 3 -> bce/ 4 -> becg the one letter difference is b == g
9. now we also know where a is becuase we located g, now we only have to locate c and f (b and e respectively)
10. lets find number 5 cdfgX -> obviously X = e -> f == e and c == b respectively

dddd
g    b
g    b
 cccc
a    e
a    e
 ffff

fdgacbe cefdb cefbgd gcbe

 dddd
g    b
g    b
 cccc
a    e
a    e
 ffff

 dddd
x    b
x    b
 cccc
x    e
x    e
 ffff

 dddd
g    b
g    b
 cccc
x    e
x    e
 ffff

 xxxx
g    b
g    b
 cccc
x    e
x    e
 xxxx
"""

from collections import defaultdict
unique_counts = {2, 4, 3, 7}


def count_digits(inpt):
    cnt = 0
    for val in inpt:
        for d in val[1]:
            if len(d) in unique_counts:
                cnt+=1

    return cnt


def decode_signal(line):
    # parse codes in the dictionary
    digits_dict = defaultdict(list)
    signals_dict = defaultdict(str)

    for digit in line[0]:
        size = len(digit)
        if size in unique_counts:
            if size == 2:
                digits_dict['1'].append(set(digit))
            elif size == 4:
                digits_dict['4'].append(set(digit))
            elif size == 3:
                digits_dict['7'].append(set(digit))
            elif size == 7:
                digits_dict['8'].append(set(digit))
        elif size == 5:
            digits_dict['2-3-5'].append(set(digit))
        elif size == 6:
            digits_dict['0-6-9'].append(set(digit))

    # find horizontal segments from 2-3-5
    horizontal_set = digits_dict['2-3-5'][0].intersection(digits_dict['2-3-5'][1]).intersection(digits_dict['2-3-5'][2])

    # find d from intersection of 4 with horizontal segments: becg/f,d,c -> g => d == c
    signals_dict['d'] = digits_dict['4'][0].intersection(horizontal_set)

    # find a from intersection of 7 with horizontal segments: bde/f,d -> a == d
    signals_dict['a'] = digits_dict['7'][0].intersection(horizontal_set)

    # obviously, last segment in the horizontal set is gggg equivalent
    signals_dict['g'] = horizontal_set - (signals_dict['d'].union(signals_dict['a']))

    # at this point we mapped all horizontal segments
    # find c and f by intersecting 1 and 7; bde/be => cf = be
    right_vertical_set = digits_dict['1'][0].intersection(digits_dict['7'][0])

    # indentify number 3 out of 3 numbers with 5 segments; among 2-3-5 find one that intersects with be
    digits_dict['3'] = [x for x in digits_dict['2-3-5'] if len(x.intersection(right_vertical_set)) == 2]

    # now the rest of the digits a and g are b and e respectively
    # now take number 3 bcdef and 4 becg, remove top and bottom
    # from 3 -> bce/ 4 -> becg the one letter difference is b == g
    temp_3 = set([x for x in digits_dict['3'][0]])
    temp_3.remove(list(signals_dict['g'])[0])
    temp_3.remove(list(signals_dict['a'])[0])
    signals_dict['b'] = digits_dict['4'][0] - temp_3

    # now we also know where e is because we located g, now we only have to locate c and f (b and e respectively)
    signals_dict['e'] = {'a','b','c','d','e','f','g'} - horizontal_set - right_vertical_set - signals_dict['b']

    # lets find number 5 cdfgX -> obviously X = e -> f == e and c == b respectively
    temp_5_X = signals_dict['a'].union(signals_dict['b']).union(signals_dict['d']).union(signals_dict['g'])
    signals_dict['f'] = [x.intersection(right_vertical_set) for x in digits_dict['2-3-5'] if len(x.difference(temp_5_X)) == 1][0]
    signals_dict['c'] = right_vertical_set - signals_dict['f']

    # I am sure there was a better way to do this,

    digits_dict['5'] = [x for x in digits_dict['2-3-5'] if len(x.difference(temp_5_X)) == 1]
    digits_dict['2'] = [x for x in digits_dict['2-3-5'] if x != digits_dict['5'][0] and x != digits_dict['3'][0]]
    digits_dict['0'] = [signals_dict['a'].union(signals_dict['b']).union(signals_dict['c']).union(signals_dict['e']).union(signals_dict['f']).union(signals_dict['g'])]
    digits_dict['6'] = [signals_dict['a'].union(signals_dict['b']).union(signals_dict['d']).union(signals_dict['e']).union(signals_dict['f']).union(signals_dict['g'])]
    digits_dict['9'] = [signals_dict['a'].union(signals_dict['b']).union(signals_dict['c']).union(signals_dict['d']).union(signals_dict['f']).union(signals_dict['g'])]

    # for k,v in digits_dict.items():
    #     print(f" {k}: {v}")
    digits_dict.pop('2-3-5')
    digits_dict.pop('0-6-9')

    code_to_digit = {"".join(sorted(list(v[0]))): k for k,v in digits_dict.items()}

    # now make the final 4 digit number
    result = ""
    for d in line[1]:
        result += code_to_digit["".join(sorted(d))]

    return int(result)


if __name__ == "__main__":
    inpt = []
    with open("day_8_input.txt") as f:
        for line in f.readlines():
            tmp = line.split('|')
            inpt.append((tmp[0].strip().split(' '), tmp[1].strip().split(' ')))

    #print(count_digits(inpt))
    total = 0
    for val in inpt:
     total += decode_signal(val)

    print(total)


