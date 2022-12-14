class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')]*n
        prices[src]=0
        for i in range(k+1):
            tempPrice = prices.copy()
            for s,d,p in flights:
                if prices[s]==float('inf'):
                    continue
                if prices[s]+p<tempPrice[d]:
                    tempPrice[d]=prices[s]+p
            prices = tempPrice
        return -1 if prices[dst]==float('inf') else prices[dst]
if __name__ == '__main__':
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 2
    ob = Solution()
    ans = ob.findCheapestPrice(n,flights,src,dst,k)
    print(ans)