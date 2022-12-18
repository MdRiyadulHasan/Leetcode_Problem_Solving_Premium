import random
class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val]=len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastval = self.numList[-1]
            self.numList[idx]=lastval
            self.numList.pop()
            self.numMap[lastval]=idx
            del self.numMap[val]
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
if __name__ =='__main__':
    obj = RandomizedSet()
    param_1 = obj.insert(20)
    param_2 = obj.remove(5)
    param_3 = obj.getRandom()
    param_4=obj.insert(10)
    param_5=obj.insert(20)
    param_6=obj.insert(15)
    param_7=obj.remove(20)
    param_8=obj.getRandom()
    print(param_1)
    print(param_2)
    print(param_3)
    print(param_4)
    print(param_5)
    print(param_6)
    print(param_7)
    print(param_8)