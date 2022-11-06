"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from
cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore,
there will be exactly one destination city.
"""

from typing import List


def destination_city(paths: List[List[str]]) -> str:
    dict_paths = {}
    for path in paths:
        for p in path:
            if p not in dict_paths:
                dict_paths[p] = [1, path.index(p)]
            else:
                dict_paths[p][0] += 1
    destination = ""
    for k, v in dict_paths.items():
        if v[0] == 1 and v[1] == 1:
            destination = k
    return destination


if __name__ == '__main__':
    paths = [["pYyNGfBYbm", "wxAscRuzOl"], ["kzwEQHfwce", "pYyNGfBYbm"]]
    print(destination_city(paths))
