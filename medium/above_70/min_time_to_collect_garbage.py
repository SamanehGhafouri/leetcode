"""
You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith
house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass
garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house
i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck
starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other
two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.
"""
import collections
from typing import List

def helper(garbage_type: str, index_type: List[int], travel_time, garbage) -> int:
    travel_type_total = 0
    if garbage_type in garbage[0]:
        count_G = collections.Counter(garbage[0])
        travel_type_total += count_G[garbage_type]
    if len(index_type) != 0:
        for i in range(1, len(garbage[:max(index_type)+1])):
            travel_type_total += travel_time[i - 1]
            if garbage_type in garbage[i]:
                count_G = garbage[i].count(garbage_type)
                travel_type_total += count_G
    return travel_type_total

def garbage_collection(garbage: List[str], travel: List[int]) -> int:
    indexes_G = []
    indexes_P = []
    indexes_M = []
    for i in range(len(garbage)):
        if "G" in garbage[i]:
            indexes_G.append(i)
        if "P" in garbage[i]:
            indexes_P.append(i)
        if "M" in garbage[i]:
            indexes_M.append(i)
    return helper("G", indexes_G, travel, garbage) + helper("P", indexes_P, travel, garbage) + helper("M", indexes_M, travel, garbage)



if __name__ == '__main__':
    garbage = ["GGMMP","MPMGPM","GPMP"]
    travel = [1,4]
    print(garbage_collection(garbage, travel))
