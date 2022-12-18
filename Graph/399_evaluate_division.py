from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (x,y),val in zip(equations,values):
            graph[x][y]=val
            graph[y][x]=1.0/val
        def dfs(x,y,visited):
            if x not in graph or y not in graph:
                return -1.0
            if y in graph[x]:
                return graph[x][y]
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp=dfs(i,y,visited)
                    if temp==-1:
                        continue
                    else:
                        return graph[x][i]*temp
            return -1

        res = []
        for query in queries:
            res.append(dfs(query[0],query[1],set()))

if __name__ == '__main__':
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ob = Solution()
    ans = ob.calcEquation(equations,values,queries)
    print(ans)