"""
You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i]
and words[j] are similar.
"""
import collections
from typing import List


def similar_pairs(words: List[int]) -> int:
    list_set_words = []
    for i in range(len(words)):
        list_set_words.append("".join(sorted(set(words[i]))))
    dict_same_words = collections.Counter(list_set_words)
    total_pairs = 0
    for k, v in dict_same_words.items():
        total_pairs += (v * (v - 1)) // 2
    return total_pairs


if __name__ == '__main__':
    words = ["ofwqemdbhrcckcnqvovyjwnbqxckhfohlripwumugcirazdtwo", "hsrmuokwhksqkkjblkomibcifqilkwobwcpwwkjlzohffsajrt",
             "uzvsxxbdwfohaujijxmeijbwyydgjiifcqvxfzmkqgwnkpxlpp", "ksdoiwhffhymsxebloadgyigkveizbahnbmvmxsuuxaaegxmpe",
             "fcsjnezuizcnfsuaxpmxpdivamaijvvyyqlsjsqlkifahjuanb", "odfwurhxumkpwndsppoflaualeghyscdqqwpntxokxviqmjhyq",
             "jbahicbweamnlfbljwyloparlmgqlwiootzoeqovytpapzjezn", "vsjxngyknxpkjfexdvmoikjaiccplcwtxcfrljqavatpcoeaqe",
             "lxiztvpppvsjmnnuunvdxalvzuvxlxbdnipexklmgsssyzlesb", "kbmiambdsahiptndziqysctinvdekysrsslssusqwhshpwehco",
             "wuwkvgrrshrmbtpyozgzzwiyflpiuklsepljvthmxnppaspuqt", "lkajvmdzpsxoaqzrgrhuhhmwlgwfnruxsrjolnielwcyjvvhaa",
             "imvgnslsxyqfshgmgecdrignarewusftipgjpteocnlqsfkdcy"]
    print(similar_pairs(words))
