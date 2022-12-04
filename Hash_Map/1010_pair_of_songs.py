class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        total_pairs = 0
        hash = {}
        for num in time:
            modNum = num%60
            if modNum ==0:
               if 0 in hash:
                   total_pairs+=hash[0]
            elif (60-modNum) in hash:
                total_pairs+=hash[60-modNum]
            if modNum in hash:
                hash[modNum]+=1
            else: 
                hash[modNum] = 1
        return total_pairs
if __name__ == '__main__':
    time = [60,30,20,150,100,30,120,40]
    ob = Solution()
    ans = ob.numPairsDivisibleBy60(time)
    print(ans)