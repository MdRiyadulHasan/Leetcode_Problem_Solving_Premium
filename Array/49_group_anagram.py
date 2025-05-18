def anagrams(strs):
    from collections import defaultdict
    dic = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        dic[key].append(word)
    return list(dic.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagrams(strs))