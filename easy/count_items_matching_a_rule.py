"""
You are given an array items, where each items[i] = [typei, colori, namei]
describes the type, color, and name of the ith item. You are also given a rule represented
by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

* ruleKey == "type" and ruleValue == typei.
* ruleKey == "color" and ruleValue == colori.
* ruleKey == "name" and ruleValue == namei.

Return the number of items that match the given rule.
"""
from typing import List


def count_matches(items: List[List[str]], rule_key: str, rule_value: str) -> int:

    count = 0
    for item in range(len(items)):

        if rule_key == "type" and items[item][0] == rule_value or \
                rule_key == "color" and items[item][1] == rule_value or \
                rule_key == "name" and items[item][2] == rule_value:
            count += 1
        else:
            count += 0
    return count


if __name__ == '__main__':
    items_li = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    rule_k = "color"
    rule_v = "silver"

    items_li_2 = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
    rule_ke = "type"
    rule_va = "phone"

    print(count_matches(items_li_2, rule_ke, rule_va))
