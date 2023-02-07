"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


def merge_two_lists(list1, list2):
    merged_list = []
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    if len(list1) == 0 and len(list2) == 0:
        return []

    for i, j in zip(range(len(list1)), range(len(list2))):

        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            merged_list.append(list2[j])
    return merged_list


if __name__ == '__main__':
    list1 = []
    list2 = [0]
    print(merge_two_lists(list1, list2))
