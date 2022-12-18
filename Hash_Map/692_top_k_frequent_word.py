class Solution:
    def topKFrequent(self, words, k: int):
        dict = {}
        for word in words:
            if word in dict:
                dict[word]+=1
            else:
                dict[word]=1
        res = sorted(dict, key = lambda x: (-dict[x],x))
        return res[:k]
if __name__ == '__main__':
     words = ["i","love","leetcode","i","love","coding"]
     k = 2
     ob = Solution()
     ans = ob.topKFrequent(words,k)

     print(ans)