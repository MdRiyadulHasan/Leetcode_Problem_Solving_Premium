def longest(s):
    l = 0
    char_set = set()
    res = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l+=1
        res =max(r-l+1, res)
        char_set.add(s[r])
    return res 
s = "abcabcbb"
print(longest(s)) 