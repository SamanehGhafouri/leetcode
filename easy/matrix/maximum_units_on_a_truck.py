"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where
 boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can
choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
"""
from typing import List


def maximum_units(box_types: List[List[int]], truck_size: int) -> int:
    max_total_units = 0
    box_types.sort(key=lambda x: x[1])
    box_types.reverse()
    for box_type in box_types:
        if truck_size < 0:
            return max_total_units
        diff = truck_size - box_type[0]
        if diff > 0:
            max_total_units += (box_type[0] * box_type[1])
        else:
            max_total_units += (truck_size * box_type[1])
        truck_size = diff
    return max_total_units


if __name__ == '__main__':
    box_t = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truck_s = 10
    print(maximum_units(box_t, truck_s))
