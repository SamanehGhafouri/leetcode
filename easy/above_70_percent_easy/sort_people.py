from typing import List


def sort_people(names: List[str], heights: List[int]) -> List[str]:
    list_tuples = []
    for name, height in zip(names, heights):
        list_tuples.append((name, height))
    list_tuples.sort(key=lambda x: x[1])
    list_tuples.reverse()
    list_tuples = [name[0] for name in list_tuples]
    return list_tuples


if __name__ == '__main__':
    nms = ["Mary", "John", "Emma"]
    hts = [180, 165, 170]
    print(sort_people(nms, hts))
