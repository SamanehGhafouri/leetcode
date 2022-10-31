"""
There are n rings and each ring is either red, green, or blue. The rings are distributed across ten
rods labeled from 0 to 9.

You are given a string rings of length 2n that describes the n rings that are placed onto the rods.
Every two characters in rings forms a color-position pair that is used to describe each ring where:

The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a
green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

Return the number of rods that have all three colors of rings on them.
"""


def count_points(rings: str) -> int:
    dict_num_colors = {}
    for i in range(0,len(rings) - 1, 2):
        if rings[i + 1] not in dict_num_colors:
            dict_num_colors[rings[i + 1]] = [rings[i]]
        else:
            dict_num_colors[rings[i + 1]].append(rings[i])

    count = 0
    for k, v in dict_num_colors.items():
        set_v = set(v)
        if len(set_v) > 2 and "R" in set_v and "B" in set_v and "G" in set_v:
            count += 1
        else:
            count += 0
    return count


if __name__ == '__main__':
    st = "G4"
    print(count_points(st))
