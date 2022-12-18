class Solution:
    def hIndex(self, citations):
        citations.sort(key=lambda x:-x)
        for h in range(len(citations)):
            if h+1>citations[h]:
                return h
        return len(citations)
if __name__ == '__main__':
    citations = [3,0,6,1,5]
    ob = Solution()
    ans = ob.hIndex(citations)
    print(ans)
    