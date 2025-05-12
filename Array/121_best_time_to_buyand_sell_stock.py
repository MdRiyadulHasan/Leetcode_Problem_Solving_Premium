
def maxProfit( prices) -> int:
    maxProfit = 0
    l = 0
    for r in range(1, len(prices)):
        if prices[l]<prices[r]:
            maxProfit = max(maxProfit, prices[r]-prices[l])
        else:
            l=r
    return maxProfit
prices = [7,1,5,3,6,4]
print(maxProfit(prices))